import pandas as pd
import numpy as np

csv_file_path = 'H0648_acclimation1_2023-04-20-16.41.50DLC_resnet50_Parkinson_s Mice ModelMay17shuffle1_500000.csv'

#Read the CSV file into a Pandas DataFrame, specifying dtype as str to handle mixed data types
df = pd.read_csv(csv_file_path, dtype=str)

#Define the column indices for each group
group1_x_index = 1  
group1_y_index = 2  
group2_x_index = 4  
group2_y_index = 5  
group3_x_index = 7
group3_y_index = 8
group4_x_index = 10
group4_y_index = 11
group5_x_index = 13
group5_y_index = 14
group6_x_index = 16
group6_y_index = 17

#Convert the specified columns to numeric data types, excluding non-numeric values
x_values_group1 = pd.to_numeric(df.iloc[:, group1_x_index], errors='coerce')
y_values_group1 = pd.to_numeric(df.iloc[:, group1_y_index], errors='coerce')
x_values_group2 = pd.to_numeric(df.iloc[:, group2_x_index], errors='coerce')
y_values_group2 = pd.to_numeric(df.iloc[:, group2_y_index], errors='coerce')
x_values_group3 = pd.to_numeric(df.iloc[:, group3_x_index], errors='coerce')
y_values_group3 = pd.to_numeric(df.iloc[:, group3_y_index], errors='coerce')
x_values_group4 = pd.to_numeric(df.iloc[:, group4_x_index], errors='coerce')
y_values_group4 = pd.to_numeric(df.iloc[:, group4_y_index], errors='coerce')
x_values_group5 = pd.to_numeric(df.iloc[:, group5_x_index], errors='coerce')
y_values_group5 = pd.to_numeric(df.iloc[:, group5_y_index], errors='coerce')
x_values_group6 = pd.to_numeric(df.iloc[:, group6_x_index], errors='coerce')
y_values_group6 = pd.to_numeric(df.iloc[:, group6_y_index], errors='coerce')

#Filter out rows with non-numeric values
valid_rows_group1 = ~x_values_group1.isnull() & ~y_values_group1.isnull()
valid_rows_group2 = ~x_values_group2.isnull() & ~y_values_group2.isnull()
valid_rows_group3 = ~x_values_group3.isnull() & ~y_values_group3.isnull()
valid_rows_group4 = ~x_values_group4.isnull() & ~y_values_group4.isnull()
valid_rows_group5 = ~x_values_group5.isnull() & ~y_values_group5.isnull()
valid_rows_group6 = ~x_values_group6.isnull() & ~y_values_group6.isnull()

#Get the time or frame column 
time_column = pd.to_numeric(df.iloc[:, 0], errors='coerce')

#Calculate the time differences between consecutive frames
time_diff = time_column.diff()

#Calculate the X and Y speed for each group
speed_group1_x = (x_values_group1.diff() / time_diff)[valid_rows_group1]
speed_group1_y = (y_values_group1.diff() / time_diff)[valid_rows_group1]
speed_group2_x = (x_values_group2.diff() / time_diff)[valid_rows_group2]
speed_group2_y = (y_values_group2.diff() / time_diff)[valid_rows_group2]
speed_group3_x = (x_values_group3.diff() / time_diff)[valid_rows_group3]
speed_group3_y = (y_values_group3.diff() / time_diff)[valid_rows_group3]
speed_group4_x = (x_values_group4.diff() / time_diff)[valid_rows_group4]
speed_group4_y = (y_values_group4.diff() / time_diff)[valid_rows_group4]
speed_group5_x = (x_values_group5.diff() / time_diff)[valid_rows_group5]
speed_group5_y = (y_values_group5.diff() / time_diff)[valid_rows_group5]
speed_group6_x = (x_values_group6.diff() / time_diff)[valid_rows_group6]
speed_group6_y = (y_values_group6.diff() / time_diff)[valid_rows_group6]


#Calculate the distance traveled for each group
distance_group1 = np.sqrt((x_values_group1.diff()**2 + y_values_group1.diff()**2))[valid_rows_group1]
distance_group2 = np.sqrt((x_values_group2.diff()**2 + y_values_group2.diff()**2))[valid_rows_group2]
distance_group3 = np.sqrt((x_values_group3.diff()**2 + y_values_group3.diff()**2))[valid_rows_group3]
distance_group4 = np.sqrt((x_values_group4.diff()**2 + y_values_group4.diff()**2))[valid_rows_group4]
distance_group5 = np.sqrt((x_values_group5.diff()**2 + y_values_group5.diff()**2))[valid_rows_group5]
distance_group6 = np.sqrt((x_values_group6.diff()**2 + y_values_group6.diff()**2))[valid_rows_group6]

#Calculate acceleration
acceleration_group1 = np.sqrt((x_values_group1.diff()**2 + y_values_group1.diff()**2)).diff()[valid_rows_group1]
acceleration_group2 = np.sqrt((x_values_group2.diff()**2 + y_values_group2.diff()**2)).diff()[valid_rows_group2]
acceleration_group3 = np.sqrt((x_values_group3.diff()**2 + y_values_group3.diff()**2)).diff()[valid_rows_group3]
acceleration_group4 = np.sqrt((x_values_group4.diff()**2 + y_values_group4.diff()**2)).diff()[valid_rows_group4]
acceleration_group5 = np.sqrt((x_values_group5.diff()**2 + y_values_group5.diff()**2)).diff()[valid_rows_group5]
acceleration_group6 = np.sqrt((x_values_group6.diff()**2 + y_values_group6.diff()**2)).diff()[valid_rows_group6]

#Calculate the jerk for each group
jerk_group1 = np.sqrt((x_values_group1.diff()**2 + y_values_group1.diff()**2)).diff().diff()[valid_rows_group1]
jerk_group2 = np.sqrt((x_values_group2.diff()**2 + y_values_group2.diff()**2)).diff().diff()[valid_rows_group2]
jerk_group3 = np.sqrt((x_values_group3.diff()**2 + y_values_group3.diff()**2)).diff().diff()[valid_rows_group3]
jerk_group4 = np.sqrt((x_values_group4.diff()**2 + y_values_group4.diff()**2)).diff().diff()[valid_rows_group4]
jerk_group5 = np.sqrt((x_values_group5.diff()**2 + y_values_group5.diff()**2)).diff().diff()[valid_rows_group5]
jerk_group6 = np.sqrt((x_values_group6.diff()**2 + y_values_group6.diff()**2)).diff().diff()[valid_rows_group6]

#Calculate the direction for each group
direction_group1 = np.arctan2(y_values_group1.diff(), x_values_group1.diff())[valid_rows_group1]
direction_group2 = np.arctan2(y_values_group2.diff(), x_values_group2.diff())[valid_rows_group2]
direction_group3 = np.arctan2(y_values_group3.diff(), x_values_group3.diff())[valid_rows_group3]
direction_group4 = np.arctan2(y_values_group4.diff(), x_values_group4.diff())[valid_rows_group4]
direction_group5 = np.arctan2(y_values_group5.diff(), x_values_group5.diff())[valid_rows_group5]
direction_group6 = np.arctan2(y_values_group6.diff(), x_values_group6.diff())[valid_rows_group6]


output_df = pd.DataFrame({
    'Group': ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6'],
    'Speed (X)': [speed_group1_x, speed_group2_x, speed_group3_x,
                   speed_group4_x, speed_group5_x, speed_group6_x],
    'Speed (Y)': [speed_group1_y, speed_group2_y, speed_group3_y,
                   speed_group4_y, speed_group5_y, speed_group6_y],
    'Distance': [distance_group1, distance_group2, distance_group3,
                 distance_group4, distance_group5, distance_group6],
    'Acceleration': [acceleration_group1, acceleration_group2, acceleration_group3,
                     acceleration_group4, acceleration_group5, acceleration_group6],
    'Jerk': [jerk_group1, jerk_group2, jerk_group3, jerk_group4, jerk_group5, jerk_group6],
    'Direction': [direction_group1, direction_group2, direction_group3,
                  direction_group4, direction_group5, direction_group6]
})

#Define the output CSV file path
output_csv_path = 'output_data.csv'

#Save the DataFrame to a CSV file
output_df.to_csv(output_csv_path, index=False)

print("Output data saved to:", output_csv_path)






