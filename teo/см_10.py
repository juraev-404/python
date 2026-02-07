import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

n = 4
p = 5/6

P_H1 = (1-p)**n
P_H2 = n * p * (1-p)**3

X = sts.binom(n, p)

P_H = np.array([X.pmf(k) for k in range(n+1)])
print(P_H)

p_A_H = np.array([(4/5)**k for k in range(n+1)])
print(p_A_H)

PA = sum(P_H * p_A_H)
print(PA)

Y = sts.binom(n, 1/2)
print(Y.pmf(2))

S = np.array([i for i in range(10, 100) if sp.isprime(i)==True])
print(S)

n = len(S)
X = np.random.choice(S, n, replace=True)
print(X)

G_X = 1
n = len(X)
for i in range(n):
    G_X *= i**(1/n)
print(G_X)

X = np.array([2,1,1,2,1,2,2,3,2,2])

N = len(X)
n = 5
X0_gen = X.mean()
E_X_sr = X0_gen
print(E_X_sr)

Var_X = np.var(X)
print(Var_X)

Var_X_sr = Var_X/n * (N-n)/(N - 1)
print(Var_X_sr)

