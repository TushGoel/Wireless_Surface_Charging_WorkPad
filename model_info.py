outlier_params = {
    'S1': (6236.092492883286, 206.78490423105308),
    'S2': (19658.116503078705, 1389.1548967225403),
    'S3': (9825.54097781029, 1403.7563752999424),
    'S4': (16032.8679574245, 1125.1370183681693)
}

outliers_limits = {
    'S1': (outlier_params['S1'][0] + (3 * outlier_params['S1'][1]),
           outlier_params['S1'][0] - (3 * outlier_params['S1'][1])),
    'S2': (outlier_params['S2'][0] + (3 * outlier_params['S2'][1]),
           outlier_params['S2'][0] - (3 * outlier_params['S2'][1])),
    'S3': (outlier_params['S3'][0] + (3 * outlier_params['S3'][1]),
           outlier_params['S3'][0] - (3 * outlier_params['S3'][1])),
    'S4': (outlier_params['S4'][0] + (3 * outlier_params['S4'][1]),
           outlier_params['S4'][0] - (3 * outlier_params['S4'][1]))
}

PATH = {
    'Transform': '/home/pi/Desktop/CoilOS_Feb_End/PythonOpt/Models_2020_02_28/Scaler_29022020.pkl',
    'Angle': ('/home/pi/Desktop/CoilOS_Feb_End/PythonOpt/Models_2020_02_28/Angle_Predictor_Arch.json',
              '/home/pi/Desktop/CoilOS_Feb_End/PythonOpt/Models_2020_02_28/Angle_Predictor_Weights.h5'),
    'Location': ('/home/pi/Desktop/CoilOS_Feb_End/PythonOpt/Models_2020_02_28/Coordinate_Predictor_Arch.json',
                 '/home/pi/Desktop/CoilOS_Feb_End/PythonOpt/Models_2020_02_28/Coordinates_Predictor_Weights.h5')
}

classes = (0, 304, 305, 306, 704, 705, 706)

## Mobile 1
# x_axis = list(range(1, 9))
# y_axis = list(range(0, 11))
# grid_m1 = [(x, y) for x in x_axis for y in y_axis]
# print(grid_m1)
# grid_device = {"Mobile 1": grid_m1}



            