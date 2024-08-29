import glob
import csv


# Phrase to search for
datasets = ['ConfLongDemo_JSI', 'Healthy_Older_People', 'User_Identification_From_Walking']
methods = ['GRU', 'LSTM', 'BiLSTM', 'ConvLSTM', 'Fusion-Averagin', 'Fusion-MV']

for dataset in datasets:
    for method in methods:
        max_f1 = 0.0
        best_filename = ''
        best_row = ''

        # Loop through all CSV files in directory
        for filename in glob.glob('non_dup_statistics.csv'):
            # Open the CSV file
            with open(filename, 'r') as f:

                # Iterate over rows
                reader = csv.DictReader(f)
                for row in reader:

                    if dataset in row['dataset'] and method in row['inner_classifier']:
                        if float(row['f1_mean']) > max_f1:
                            max_f1 = float(row['f1_mean'])
                            best_filename = filename
                            best_row = row

        print(dataset, method, best_filename)
        print("f1", round(float(best_row['f1_mean']) * 100, 2), "($\pm$", round(float(best_row['f1_std']), 2),
              ")")
        print("mse", round(float(best_row['mse_loss_mean']), 4), "($\pm$", round(float(best_row['mse_loss_std']), 3), ")")

        print("recall", round(float(best_row['recall_mean']) * 100, 2), "($\pm$",
              round(float(best_row['recall_std']), 2), ")")
        print("precision", round(float(best_row['precision_mean']) * 100, 2), "($\pm$",
              round(float(best_row['precision_std']), 2), ")")
        print("accuracy", round(float(best_row['accuracy_mean']) * 100, 2), "($\pm$",
              round(float(best_row['accuracy_std']), 2), ")")
