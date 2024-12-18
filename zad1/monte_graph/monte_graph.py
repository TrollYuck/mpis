import numpy as np
import matplotlib.pyplot as plt

with open('monte_carlo.txt', 'r') as f:
    data = f.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

y = data_array[:,0]
x = data_array[:,1]

# Define the value for the horizontal line
horizontal_line_value = 0.2  # Change this to your desired value
k = 50
f = "f_3"


# Find unique x values
unique_x = np.unique(x)
min_y_indices = []


# For each unique x value, find the closest y value to the horizontal line
for unique in unique_x:
    indices = np.where(x == unique)[0]  # Get indices of the current unique x values
    y_values = y[indices]                # Corresponding y values
    distances = np.abs(y_values - horizontal_line_value)  # Calculate distances
    min_index = indices[np.argmin(distances)]  # Find index of the closest point
    min_y_indices.append(y[min_index])

mean_y = np.array([np.mean(y[x == unique]) for unique in unique_x])

min_y = np.array(mean_y)
min_x = np.fromfile('ref.txt', np.int64, -1, '\n', 0)




# Create the plot
plt.figure(figsize=(16, 11), dpi=300)
plt.scatter(x, y, color='blue', s=10, zorder=1) # Use scatter to display points without connecting them
plt.scatter(min_x, min_y, color='red', s=15, zorder=2)
plt.axhline(y=horizontal_line_value, color='green', linestyle='solid', label=f'Real value the Integral: {horizontal_line_value}', linewidth=2)
plt.title(f'{f} k = {k}')
plt.xlabel('n')
plt.ylabel('C')

plt.minorticks_on()

plt.grid(False)
plt.legend()
plt.savefig(f'{f}_k{k}2.png', format='png', dpi=300)
plt.show()