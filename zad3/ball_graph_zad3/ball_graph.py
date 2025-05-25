import numpy as np
import matplotlib.pyplot as plt

with open('D1.txt', 'r') as d1:
    data = d1.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

x = data_array[:,0]
unique_x = np.unique(x)

y1 = data_array[:,1]
y1_mean = np.array([np.mean(y1[x == unique]) for unique in unique_x])

with open('D2.txt', 'r') as d2:
    data = d2.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

y2 = data_array[:,1]
y2_mean = np.array([np.mean(y2[x == unique]) for unique in unique_x])

f1 = np.divide(np.log(unique_x), np.log(np.log(unique_x)))
f2 = np.divide(np.log(np.log(unique_x)), np.log(2))

d1f1 = np.divide(y1_mean, f1)
d2f2 = np.divide(y2_mean, f2)



plt.figure(figsize=(16,11),dpi=300)
plt.xlabel('n')
plt.ylabel('Relation')
plt.yscale('log') #dobór skali
#plt.xscale('log')
plt.title('l_n (d=1) / f1') #dobór tytułu

#plt.scatter(x, y2, label='max', s = 5,  zorder = 1) #naniesienie punktów na wykres
#plt.scatter(unique_x, yb_mean, color='red', label='Mean for each' , zorder = 2) #naniesienie funkcji na wykres

plt.plot(unique_x, d1f1, color='green', label='l_n (d=1) / f1' , zorder = 3)
plt.plot(unique_x, y1_mean, color='red', label='l_n (d=1)' , zorder = 3)
plt.plot(unique_x, f1, color='blue', label='f1' , zorder = 3)

#plt.plot(unique_x, e3_graph, color='blue', label='e(n)/(n ln ln n)' , zorder = 4)

plt.minorticks_on() #włączenie podziałki pomocniczej
plt.legend() #włączenie legendy
plt.grid(True) #włączenie siatki

plt.savefig('D1f1log.png', format='png', dpi=300, transparent=True) #zapis wykresu do pliku
plt.show()
