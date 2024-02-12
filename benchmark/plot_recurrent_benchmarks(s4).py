import time
import datetime
import pandas
import plotly.express as px
import numpy as np
import os

from benchmark.dataset_information import problems


def string_seconds(x):
    x = time.strptime(x, '%H:%M:%S')
    return datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()


data = pandas.read_csv("non_dup_statistics.csv")
datasets = np.unique(data.dataset)

classifiers = ["GRU", "LSTM", "BiLSTM", "ConvLSTM", "Fusion-Averagin", "Fusion-MV"]
classifiers_title = ["GRU", "LSTM", "BiLSTM", "ConvLSTM", "Fusion (Averaging)", "Fusion (Majority Voting)"]
for dataset in datasets:
    for classifier, ctitle in zip(classifiers, classifiers_title):
        data_ds = data[data.dataset == dataset]
        data_ds = data_ds[data_ds.inner_classifier == classifier]

        sr = problems[dataset]['sample_rate']
        segments_times = data_ds.segments_time.to_numpy()
        decision_times = data_ds.decision_time.to_numpy()
        data_ds["w"] = np.array([string_seconds(segments_times[j]) * sr for j in range(len(segments_times))])
        data_ds["s"] = np.array([string_seconds(decision_times[j]) * sr for j in range(len(decision_times))])

        if data_ds.shape[0] == 0:
            continue

        max_id = data_ds.f1_mean.argmax()
        print(dataset, classifier,
              data_ds.segments_time.iloc[max_id],
              data_ds.decision_time.iloc[max_id],
              str(round(data_ds.f1_mean.iloc[max_id] * 100, 2)) + " ($\pm$ " +
              str(round(data_ds.f1_std.iloc[max_id], 2)) + ")",
              str(round(data_ds.mse_loss_mean.iloc[max_id], 4)) + " ($\pm$ " +
              str(round(data_ds.mse_loss_std.iloc[max_id], 3)) + ")")

        fig = px.scatter_3d(data_ds, x="s", y="w", z="f1_mean", color="f1_mean", title=ctitle,
                            range_color=(0, 1), opacity=0.7)
        fig.update_traces(marker_size=4)

        labels = dict(
            xaxis_title='s',
            yaxis_title='w',
            zaxis_title='mean f1')
        camera = dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.5, y=1.5, z=1.5)
        )
        fig.update_layout(scene_camera=camera, showlegend=False, title_x=0.5, title_y=0.92,
                          scene=dict(
                              zaxis=dict(nticks=20, range=[0, 1]),
                              xaxis_title='s',
                              yaxis_title='w',
                              zaxis_title='mean f1'
                          ))
        fig.update_coloraxes(showscale=False)

        fig.update_layout(
            height=500, width=500,
            margin=dict(l=0, r=0, t=0, b=0),
        )

        if not os.path.exists("images/" + dataset + "/"):
            os.mkdir("images/" + dataset + "/")
        fig.write_image("images/" + dataset + "/" + classifier + ".png")
        # fig.show()