import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import os
import csv


csv_file_path = 'H0648//H0648_acclimation1_2023-04-20-16.41.50DLC_resnet50_Parkinson_s Mice ModelMay17shuffle1_500000.csv'

# Read the CSV file into a Pandas DataFrame, specifying dtype as str to handle mixed data types
df = pd.read_csv(csv_file_path, dtype=str)

# Define the column indices for each group
group1_x_index = 1  
group1_y_index = 2
group1_likelihood_index = 3
group2_x_index = 4  
group2_y_index = 5
group2_likelihood_index = 6
group3_x_index = 7
group3_y_index = 8
group3_likelihood_index = 9
group4_x_index = 10
group4_y_index = 11
group4_likelihood_index = 12
group5_x_index = 13
group5_y_index = 14
group5_likelihood_index = 15
group6_x_index = 16
group6_y_index = 17
group6_likelihood_index = 18


# Convert the specified columns to numeric data types, excluding non-numeric values
x_values_group1 = pd.to_numeric(df.iloc[:, group1_x_index], errors='coerce')
y_values_group1 = pd.to_numeric(df.iloc[:, group1_y_index], errors='coerce')
likelihood_values_group1 = pd.to_numeric(df.iloc[:, group1_likelihood_index], errors='coerce')
x_values_group2 = pd.to_numeric(df.iloc[:, group2_x_index], errors='coerce')
y_values_group2 = pd.to_numeric(df.iloc[:, group2_y_index], errors='coerce')
likelihood_values_group2 = pd.to_numeric(df.iloc[:, group2_likelihood_index], errors='coerce')
x_values_group3 = pd.to_numeric(df.iloc[:, group3_x_index], errors='coerce')
y_values_group3 = pd.to_numeric(df.iloc[:, group3_y_index], errors='coerce')
likelihood_values_group3 = pd.to_numeric(df.iloc[:, group3_likelihood_index], errors='coerce')
x_values_group4 = pd.to_numeric(df.iloc[:, group4_x_index], errors='coerce')
y_values_group4 = pd.to_numeric(df.iloc[:, group4_y_index], errors='coerce')
likelihood_values_group4 = pd.to_numeric(df.iloc[:, group4_likelihood_index], errors='coerce')
x_values_group5 = pd.to_numeric(df.iloc[:, group5_x_index], errors='coerce')
y_values_group5 = pd.to_numeric(df.iloc[:, group5_y_index], errors='coerce')
likelihood_values_group5 = pd.to_numeric(df.iloc[:, group5_likelihood_index], errors='coerce')
x_values_group6 = pd.to_numeric(df.iloc[:, group6_x_index], errors='coerce')
y_values_group6 = pd.to_numeric(df.iloc[:, group6_y_index], errors='coerce')
likelihood_values_group6 = pd.to_numeric(df.iloc[:, group6_likelihood_index], errors='coerce')

# Filter out rows with non-numeric values
valid_rows_group1 = ~x_values_group1.isnull() & ~y_values_group1.isnull() & ~likelihood_values_group1.isnull()
valid_rows_group2 = ~x_values_group2.isnull() & ~y_values_group2.isnull() & ~likelihood_values_group2.isnull()
valid_rows_group3 = ~x_values_group3.isnull() & ~y_values_group3.isnull() & ~likelihood_values_group3.isnull()
valid_rows_group4 = ~x_values_group4.isnull() & ~y_values_group4.isnull() & ~likelihood_values_group4.isnull()
valid_rows_group5 = ~x_values_group5.isnull() & ~y_values_group5.isnull() & ~likelihood_values_group5.isnull()
valid_rows_group6 = ~x_values_group6.isnull() & ~y_values_group6.isnull() & ~likelihood_values_group6.isnull()

for i in range(1, len(likelihood_values_group1) - 1):
    if likelihood_values_group1[i] < 0.5:
        if likelihood_values_group1[i - 1] > 0.5 and likelihood_values_group1[i + 1] > 0.5:
            # Average the x and y values of neighboring points
            x_avg = (x_values_group1[i - 1] + x_values_group1[i + 1]) / 2
            y_avg = (y_values_group1[i - 1] + y_values_group1[i + 1]) / 2

            # Replace the point with the averaged values
            x_values_group1[i] = x_avg
            y_values_group1[i] = y_avg

for i in range(1, len(likelihood_values_group2) - 1):
    if likelihood_values_group2[i] < 0.5:
        if likelihood_values_group2[i - 1] > 0.5 and likelihood_values_group2[i + 1] > 0.5:
            # Average the x and y values of neighboring points
            x_avg = (x_values_group2[i - 1] + x_values_group2[i + 1]) / 2
            y_avg = (y_values_group2[i - 1] + y_values_group2[i + 1]) / 2

            # Replace the point with the averaged values
            x_values_group2[i] = x_avg
            y_values_group2[i] = y_avg

for i in range(1, len(likelihood_values_group3) - 1):
    if likelihood_values_group3[i] < 0.5:
        if likelihood_values_group3[i - 1] > 0.5 and likelihood_values_group3[i + 1] > 0.5:
            # Average the x and y values of neighboring points
            x_avg = (x_values_group3[i - 1] + x_values_group3[i + 1]) / 2
            y_avg = (y_values_group3[i - 1] + y_values_group3[i + 1]) / 2

            # Replace the point with the averaged values
            x_values_group3[i] = x_avg
            y_values_group3[i] = y_avg

for i in range(1, len(likelihood_values_group4) - 1):
    if likelihood_values_group4[i] < 0.5:
        if likelihood_values_group4[i - 1] > 0.5 and likelihood_values_group4[i + 1] > 0.5:
            # Average the x and y values of neighboring points
            x_avg = (x_values_group4[i - 1] + x_values_group4[i + 1]) / 2
            y_avg = (y_values_group4[i - 1] + y_values_group4[i + 1]) / 2

            # Replace the point with the averaged values
            x_values_group4[i] = x_avg
            y_values_group4[i] = y_avg

for i in range(1, len(likelihood_values_group5) - 1):
    if likelihood_values_group5[i] < 0.5:
        if likelihood_values_group5[i - 1] > 0.5 and likelihood_values_group5[i + 1] > 0.5:
            # Average the x and y values of neighboring points
            x_avg = (x_values_group5[i - 1] + x_values_group5[i + 1]) / 2
            y_avg = (y_values_group5[i - 1] + y_values_group5[i + 1]) / 2

            # Replace the point with the averaged values
            x_values_group5[i] = x_avg
            y_values_group5[i] = y_avg

for i in range(1, len(likelihood_values_group6) - 1):
    if likelihood_values_group6[i] < 0.5:
        if likelihood_values_group6[i - 1] > 0.5 and likelihood_values_group6[i + 1] > 0.5:
            # Average the x and y values of neighboring points
            x_avg = (x_values_group6[i - 1] + x_values_group6[i + 1]) / 2
            y_avg = (y_values_group6[i - 1] + y_values_group6[i + 1]) / 2

            # Replace the point with the averaged values
            x_values_group6[i] = x_avg
            y_values_group6[i] = y_avg



# Plot the data for each group
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed
# Group 1
plt.plot(x_values_group1[valid_rows_group1], y_values_group1[valid_rows_group1], color='red', linewidth=1, label='Snout')
# Group 2
plt.plot(x_values_group2[valid_rows_group2], y_values_group2[valid_rows_group2], color='orange', linewidth=1, label='R_Ear')
#Group 3
plt.plot(x_values_group3[valid_rows_group3], y_values_group3[valid_rows_group3], color='yellow', linewidth=1, label='L_Ear')
#Group 4
plt.plot(x_values_group4[valid_rows_group4], y_values_group4[valid_rows_group4], color='green', linewidth=1, label='Nape')
#Group 5
plt.plot(x_values_group5[valid_rows_group5], y_values_group5[valid_rows_group5], color='blue', linewidth=1, label='Tail_Base')
#Group 6
plt.plot(x_values_group6[valid_rows_group6], y_values_group6[valid_rows_group6], color='purple', linewidth=1, label='Tail_Tip')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of Mouse Traveled')
plt.legend()  # Display the legend

plt.show()


