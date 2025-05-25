import numpy as np
import matplotlib.pyplot as plt

with open('cmp.txt', 'r') as f:
    data = f.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

x = data_array[:,0]
unique_x = np.unique(x)

cmp = data_array[:,1]
cmp_mean = np.array([np.mean(cmp[x == unique]) for unique in unique_x])

with open('swap.txt', 'r') as f:
    data = f.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

swap = data_array[:,1]
swap_mean = np.array([np.mean(swap[x == unique]) for unique in unique_x])

c1 = np.divide(cmp_mean, unique_x)
c2 = np.divide(cmp_mean, unique_x**2)

d1 = np.divide(swap_mean, unique_x)
d2 = np.divide(swap_mean, unique_x**2)

plt.figure(figsize=(16,11),dpi=300)
plt.xlabel('n')
plt.ylabel('value')
plt.yscale('linear') #dobór skali
plt.title('SWAP/n & SWAP/n^2') #dobór tytułu

#plt.scatter(x, swap, label = 's', s = 5, zorder = 1)

#plt.plot(unique_x, swap_mean, label = 'swap_mean', color = 'red', zorder = 2)
plt.scatter(unique_x, d1, label = 's/n', color = 'green', zorder = 3)
plt.scatter(unique_x, d2, label = 's/n^2', color = 'blue', zorder = 4)

plt.minorticks_on() #włączenie podziałki pomocniczej
plt.legend() #włączenie legendy
plt.grid(True) #włączenie siatki

#plt.savefig('pdpD.png', format='png', dpi=300, transparent=True) #zapis wykresu do pliku
plt.show()