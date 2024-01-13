problems = {'ConfLongDemo_JSI': {},
            'Healthy_Older_People': {},
            'User_Identification_From_Walking': {},
            'WISDM': {},
            }

problems['ConfLongDemo_JSI']['dataset'] = './datasets/ConfLongDemo_JSI/'
problems['ConfLongDemo_JSI']['n_classes'] = 5
problems['ConfLongDemo_JSI']['features'] = ["x", "y", "z"]
problems['ConfLongDemo_JSI']['sample_rate'] = 30
problems['ConfLongDemo_JSI']['data_length_time'] = -1
problems['ConfLongDemo_JSI']['n_h_block'] = 15
problems['ConfLongDemo_JSI']['n_train_h_block'] = 9
problems['ConfLongDemo_JSI']['n_valid_h_block'] = 2
problems['ConfLongDemo_JSI']['n_test_h_block'] = 4
problems['ConfLongDemo_JSI']['h_moving_step'] = 1
problems['ConfLongDemo_JSI']['decision_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 30, 60, 2 * 60]
problems['ConfLongDemo_JSI']['segments_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 30, 60]

problems['Healthy_Older_People']['dataset'] = './datasets/Healthy_Older_People/'
problems['Healthy_Older_People']['n_classes'] = 12
problems['Healthy_Older_People']['features'] = ["X", "Y", "Z"]
problems['Healthy_Older_People']['sample_rate'] = 1
problems['Healthy_Older_People']['data_length_time'] = -1
problems['Healthy_Older_People']['n_h_block'] = 15
problems['Healthy_Older_People']['n_train_h_block'] = 9
problems['Healthy_Older_People']['n_valid_h_block'] = 2
problems['Healthy_Older_People']['n_test_h_block'] = 4
problems['Healthy_Older_People']['h_moving_step'] = 1
problems['Healthy_Older_People']['decision_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 30, 60, 2 * 60, 3 * 60]
problems['Healthy_Older_People']['segments_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 30, 60, 2 * 60]

problems['User_Identification_From_Walking']['dataset'] = './datasets/User_Identification_From_Walking/'
problems['User_Identification_From_Walking']['n_classes'] = 13
problems['User_Identification_From_Walking']['features'] = [' x acceleration', ' y acceleration', ' z acceleration']
problems['User_Identification_From_Walking']['sample_rate'] = 32
problems['User_Identification_From_Walking']['data_length_time'] = -1
problems['User_Identification_From_Walking']['n_h_block'] = 10
problems['User_Identification_From_Walking']['n_train_h_block'] = 5
problems['User_Identification_From_Walking']['n_valid_h_block'] = 2
problems['User_Identification_From_Walking']['n_test_h_block'] = 3
problems['User_Identification_From_Walking']['h_moving_step'] = 1
problems['User_Identification_From_Walking']['decision_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                                  18, 19, 20, 21, 22, 23, 24]
problems['User_Identification_From_Walking']['segments_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

problems['WISDM']['dataset'] = './datasets/WISDM/'
problems['WISDM']['n_classes'] = 10
problems['WISDM']['features'] = ['X-accel', 'Y-accel', 'Z-accel']
problems['WISDM']['sample_rate'] = 20
problems['WISDM']['data_length_time'] = -1
problems['WISDM']['n_h_block'] = 15
problems['WISDM']['n_train_h_block'] = 9
problems['WISDM']['n_valid_h_block'] = 4
problems['WISDM']['n_test_h_block'] = 2
problems['WISDM']['h_moving_step'] = 1
problems['WISDM']['decision_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 30, 60, 2 * 60, 3 * 60, 4 * 60, 5 * 60, 6 * 60, 7 * 60,
                                       8 * 60, 9 * 60, 10 * 60]
problems['WISDM']['segments_times'] = [3, 4, 5, 6, 7, 8, 9, 10, 30, 60, 2 * 60, 3 * 60, 4 * 60, 5 * 60, 6 * 60, 7 * 60]
