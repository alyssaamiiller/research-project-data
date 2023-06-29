import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import os
import csv

csv_file_path = 'H0648_acclimation1_2023-04-20-16.41.50DLC_resnet50_Parkinson_s Mice ModelMay17shuffle1_500000.csv'

# Read the CSV file into a Pandas DataFrame, specifying dtype as str to handle mixed data types
df = pd.read_csv(csv_file_path, dtype=str)
group1LikelihoodIndex = 3
likeLihoodValues = pd.to_numeric(df.iloc[:,group1LikelihoodIndex], errors ='coerce')
validRowsgroup1 = ~likeLihoodValues.isnull()
plt.figure(figsize=(8,6))
plt.plot(likeLihoodValues[validRowsgroup1], color = 'red', linewidth = 1, label = 'Snout')
plt.xlabel('time')
plt.ylabel('likelihood')
plt.title('Likelihood')
plt.legend()

plt.show()
