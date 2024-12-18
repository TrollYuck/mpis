import numpy as np
import matplotlib.pyplot as plt

with open('Bn.txt', 'r') as B:
    data = B.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

x = data_array[:,0]
unique_x = np.unique(x)

yb = data_array[:,1]
yb_mean = np.array([np.mean(yb[x == unique]) for unique in unique_x])

with open('Cn.txt', 'r') as C:
    data = C.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

yc = data_array[:,1]
yc_mean = np.array([np.mean(yc[x == unique]) for unique in unique_x])

with open('Dn.txt', 'r') as D:
    data = D.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

yd = data_array[:,1]
yd_mean = np.array([np.mean(yd[x == unique]) for unique in unique_x])

with open('Un.txt', 'r') as U:
    data = U.read()
data_lines = data.strip().split('\n')
data_array = np.array([list(map(float, line.split())) for line in data_lines])

yu = data_array[:,1]
yu_mean = np.array([np.mean(yu[x == unique]) for unique in unique_x])

yd_c = yd - yc
yd_c_mean = np.array([np.mean(yd_c[x == unique]) for unique in unique_x])

#print(yb_mean)

################################

#podpunkt a
a1_graph = np.divide(yb_mean, unique_x)
a2_graph = np.divide(yb_mean, np.sqrt(unique_x))

#podpunkt b
b1_graph = np.divide(yu_mean, unique_x)
'''
#podpunkt c
c1_graph = np.divide(yc_mean, unique_x)
c2_graph = np.divide(yc_mean, np.multiply(unique_x, np.log(unique_x)))
c3_graph = np.divide(yc_mean, np.power(unique_x, 2))

#podpunkt d
d1_graph = np.divide(yd_mean, unique_x)
d2_graph = np.divide(yd_mean, np.multiply(unique_x, np.log(unique_x)))
d3_graph = np.divide(yd_mean, np.power(unique_x, 2))

#podpunkt e
e1_graph = np.divide(yd_c_mean, unique_x)
e2_graph = np.divide(yd_c_mean, np.multiply(unique_x, np.log(unique_x)))
e3_graph = np.divide(yd_c_mean, np.multiply(unique_x, np.log(np.log(unique_x))))

################################
'''
plt.figure(figsize=(16,11),dpi=300)
plt.xlabel('n')
plt.ylabel('M')
plt.yscale('log') #dobór skali
plt.xscale('log')
plt.title('Podpunkt B') #dobór tytułu

#plt.scatter(x, yb, label='Dn - Cn', s = 5,  zorder = 1) #naniesienie punktów na wykres

plt.plot(unique_x, a1_graph, color='red', label='b(n)/n' , zorder = 2) #naniesienie funkcji na wykres
plt.plot(unique_x, a2_graph, color='green', label='b(n)/(sqrt(n))' , zorder = 3)
#plt.plot(unique_x, e3_graph, color='blue', label='e(n)/(n ln ln n)' , zorder = 4)

plt.minorticks_on() #włączenie podziałki pomocniczej
plt.legend() #włączenie legendy
plt.grid(True) #włączenie siatki

#plt.savefig('PdpB.png', format='png', dpi=300, transparent=True) #zapis wykresu do pliku
plt.show()
