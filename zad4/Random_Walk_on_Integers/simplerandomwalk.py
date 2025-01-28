import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from tqdm import tqdm

def randomwalk(n):
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = x[i-1] + np.random.choice([-1, 1], p=[0.5, 0.5])
    return x

def empirical_cdf(data, num_bins):
    counts, bin_edges = np.histogram(data, bins=num_bins, range=(-max(data), max(data)), density=True)
    cdf = np.cumsum(counts) / sum(counts)
    return bin_edges[1:], cdf

n_values = [5, 10, 15, 20, 25, 30, 100]
k = 1000  # liczba powtórzeń

for n in tqdm(n_values):
    walks = np.array([randomwalk(n)[-1] for _ in range(k)])
    x, y = empirical_cdf(walks, num_bins=50)

    # Dystrybuanta empiryczna
    plt.figure()
    plt.plot(x, y, label=f'Empiryczna N = {n}')

    # Dystrybuanta rozkładu normalnego
    x_norm = np.linspace(-n, n, 1000)
    y_norm = norm.cdf(x_norm, loc=0, scale=np.sqrt(n))
    plt.plot(x_norm, y_norm, label=f'Normalna N = {n}', linestyle='dashed')

    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title(f'Porównanie dystrybuant dla N = {n}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'empirical_cdf_{n}.png', dpi=300, transparent=True)
    plt.show()
