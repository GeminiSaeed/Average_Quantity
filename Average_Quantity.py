import pandas as pd
import numpy as np
import os

# Set the base path to the current directory of the script
base_path = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the Data folder
data_folder_path = os.path.join(base_path, 'Data/')

# You can drop the code in the Data folder where all csv files exist. In that case comment lines 6 and 9 and also 
# Your line 26 should look like -> pd.read_csv(file_pattern.format(i)) 

# Specifying the pattern in the names of files. Here, the names of the files are "1.csv", "2.csv", ..., "100.csv".
# If your files were sequenced like "timestep_1.csv", ..., "timestep_n.csv", use file_pattern = "timestep_{}.csv".   
file_pattern = "{}.csv"

# The number of files in our directory.
file_number = 100

# Creating an empty list called 'result' where we will store the data.
result = []

# Reading files one by one from our directory as a DataFrame. 
for i in range(1, file_number + 1):
    temp = pd.read_csv(data_folder_path+file_pattern.format(i))
    # We are only interested in the values of the columns, not the labels.
    data = temp.values
    # Storing all DataFrames in the list.
    result.append(data)

# Converting the list into a 3-dimensional array where the shape of the array is (number of files, rows, columns).
result = np.array(result)

# Taking the average for each corresponding column across all files in our directory.
average = result.mean(axis=0)

# Exporting the averaged DataFrame as "Result.csv", which represents all files.
average = pd.DataFrame(data=average, columns= temp.columns)
average.to_csv("Result.csv", index=False)

#######################################

# Creating a plot for the averaged data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Extracting coordinates and our desired qunatity to represent
x = average['X (m)'].values
z = average['Z (m)'].values
velocity = average['Velocity: Magnitude (m/s)'].values

# Create grid coordinates for contour plot
xi = np.linspace(min(x), max(x), 100)
zi = np.linspace(min(z), max(z), 100)
Xi, Zi = np.meshgrid(xi, zi)

# Interpolate the velocity for new points
velocity_interpolated = griddata((x, z), velocity, (Xi, Zi), method='linear')

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
contour = ax.contourf(Xi, Zi, velocity_interpolated, 256, cmap='viridis', alpha=0.7)

# Add a color bar which maps values to colors
cbar = fig.colorbar(contour, shrink=0.5, aspect=5)
cbar.set_label('Velocity: Magnitude (m/s)')

ax.set_xlabel('X (m)')
ax.set_ylabel('Z (m)')
ax.set_title('Velocity Field')

plt.show()
