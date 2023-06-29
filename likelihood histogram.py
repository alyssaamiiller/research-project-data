import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import os
import csv

csv_file_path = 'H0719//H0719-Control1_2023-05-08-09.51.25DLC_resnet50_Parkinson_s Mice ModelMay17shuffle1_500000.csv'

# Read the CSV file into a Pandas DataFrame, specifying dtype as str to handle mixed data types
df = pd.read_csv(csv_file_path, dtype=str)
group1LikelihoodIndex = 18
likelihoodValues = pd.to_numeric(df.iloc[:, group1LikelihoodIndex], errors='coerce')
validRowsGroup1 = likelihoodValues > 0.5
print(likelihoodValues[likelihoodValues > .5].count())
plt.figure(figsize=(8, 6))
plt.hist(likelihoodValues[validRowsGroup1], bins=1000, color='red', alpha = 0.5)
plt.xlabel('Likelihood')
plt.ylabel('Frequency')
plt.title('Likelihood Histogram')
plt.yscale('log') 

plt.show()
