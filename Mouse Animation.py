import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

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

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the line objects for each group
lines = []
lines.append(ax.plot([], [], color='red', linewidth=1, label='Snout')[0])
lines.append(ax.plot([], [], color='orange', linewidth=1, label='R_Ear')[0])
lines.append(ax.plot([], [], color='yellow', linewidth=1, label='L_Ear')[0])
lines.append(ax.plot([], [], color='green', linewidth=1, label='Nape')[0])
lines.append(ax.plot([], [], color='blue', linewidth=1, label='Tail_Base')[0])
lines.append(ax.plot([], [], color='purple', linewidth=1, label='Tail_Tip')[0])

# Function to update the plot for each frame
def update(frame):
    # Update the data for each line
    lines[0].set_data(x_values_group1[:frame], y_values_group1[:frame])
    lines[1].set_data(x_values_group2[:frame], y_values_group2[:frame])
    lines[2].set_data(x_values_group3[:frame], y_values_group3[:frame])
    lines[3].set_data(x_values_group4[:frame], y_values_group4[:frame])
    lines[4].set_data(x_values_group5[:frame], y_values_group5[:frame])
    lines[5].set_data(x_values_group6[:frame], y_values_group6[:frame])
    
    return lines

# Set the axis limits
ax.set_xlim([0, 1800])  # Adjust the limits based on your data
ax.set_ylim([0, 1500])  # Adjust the limits based on your data

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100, blit=True)

# Display the animation
plt.show()

