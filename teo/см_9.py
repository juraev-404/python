import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as sts

ABC = np.array([-208, 94, -739, -58, 179, 78, -237, 23, 236, 277, 301, 241, -165, 67, 211, -369, 666, 84, 
220, -83, 166, -496, 205, 108, 45, 197, -452, -268, 150, 27, -206, -7, -263, -7, -611, 556, -620, 302, 403, -289])

mu = ABC.mean()
sigma = ABC.std()

X = sts.norm(mu, sigma)

L = X.ppf(0.25)
H = X.ppf(0.75)

N = len(ABC[(ABC >= L) & (ABC <= H)])

from statsmodels.distributions.empirical_distribution import ECDF

F_exp = ECDF(ABC)
plt.figure(figsize=(16, 10))
x = np.linspace(X.ppf(0.01), X.ppf(0.99), 500)
plt.plot(x, X.cdf(x), label='Теоретическая функция распределения', color='red')
plt.plot(x, F_exp(x), label='Эмпирическая функция распределения', color='blue')
plt.legend()
plt.grid()
plt.show()

d = sts.kstest(ABC, X.cdf)[0]

