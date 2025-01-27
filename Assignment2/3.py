import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('weight-height.csv')
# print(df.columns)

length = df['Height']
weight = df['Weight']

# convert length to cm and weight to kg

length_cm = length * 2.54
weight_kg = weight * 0.453592

# Calculate the means of length and weight 
mean_length_cm = np.mean(length_cm)
mean_weight_kg = np.mean(weight_kg)

print(f'Mean Length: {mean_length_cm}')
print(f'Mean Weight: {mean_weight_kg}')

# Draw a histogram of length
plt.hist(length_cm, bins=20, color='crimson', edgecolor='black')
plt.title('Histogram of Length (in cm)')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()