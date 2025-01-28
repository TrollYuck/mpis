import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def randomwalk(n):
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = x[i-1] + np.random.choice([-1, 1], p=[0.5, 0.5])
    return x

def calculate_pn(n, k):
    pn_values = []
    for _ in tqdm(range(k), desc=f'Generating for N={n}'):
        walk = randomwalk(n)
        Dn = np.where((walk > 0) | (np.roll(walk, 1) > 0), 1, 0)
        Dn[0] = 1 if walk[0] > 0 else 0  # Handle the first element separately
        LN = np.sum(Dn)
        pn = LN / n
        pn_values.append(pn)
    return pn_values

def plot_histogram(pn_values, n):
    plt.figure()
    plt.hist(pn_values, bins=20, density=True, alpha=0.6, color='g')
    plt.xlabel('P_N')
    plt.ylabel('Density')
    plt.title(f'Histogram frakcji czasu P_N dla N = {n}')
    plt.grid(True)
    plt.savefig(f'histogram_{n}.png', dpi=300, transparent=True)
    plt.show()

n_values = [100, 1000, 10000]
k = 5000  # liczba powtórzeń

for n in n_values:
    PN_values = calculate_pn(n, k)
    plot_histogram(PN_values, n)