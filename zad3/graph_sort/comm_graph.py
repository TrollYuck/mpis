import numpy as np
import matplotlib.pyplot as plt

with open('distorted_comm01.csv', 'r') as f:
    data = f.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split(','))) for line in data_lines])

x = data_array[:,0]
unique_x = np.unique(x)

dc01 = data_array[:,1]
dc01_mean = np.array([np.mean(dc01[x == unique]) for unique in unique_x])

with open('distorted_comm05.csv', 'r') as f:
    data = f.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split(','))) for line in data_lines])

dc05 = data_array[:,1]
dc05_mean = np.array([np.mean(dc05[x == unique]) for unique in unique_x])

plt.figure(figsize=(16,11),dpi=300)
plt.xlabel('n')
plt.ylabel('T_n')
plt.yscale('linear') #dobór skali
plt.title('Min T_n for p = 0.5 and p = 0.1') #dobór tytułu

plt.scatter(x, dc05, label = 'T, p = 0.5', s = 5, zorder = 1)
plt.scatter(x, dc01, label = 'T, p = 0.1', color = 'green', s = 5, zorder = 1)

plt.plot(unique_x, dc05_mean, label = 'Mean for p = 0.5', color = 'red', zorder = 2)
plt.plot(unique_x, dc01_mean, label = 'Mean for p = 0.1', color = 'red', zorder = 2)

plt.minorticks_on() #włączenie podziałki pomocniczej
plt.legend() #włączenie legendy
plt.grid(True) #włączenie siatki

plt.savefig('DC05and01.png', format='png', dpi=300, transparent=True) #zapis wykresu do pliku
plt.show()