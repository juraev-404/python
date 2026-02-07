import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

sigma = 32.4
n = 9
x_sr = 187.9
gamma = 0.8

se = sigma/math.sqrt(n)
z_gamma = sts.norm.ppf((1+gamma)/2)
print(z_gamma)

delta = z_gamma*se
print(x_sr-delta, x_sr+delta)

print(sts.norm.interval(gamma, x_sr, se))

gamma1 = 2*sts.norm.cdf((x_sr - 165.8)*math.sqrt(n)/sigma)-1
print(gamma1)

xi = np.array([-2,1,2,3,4,5])
ni = np.array([2,1,2,2,2,1])

n = sum(ni)
x_sr = sum(xi * ni)/n
s_2 = sum((xi-x_sr)**2*ni)/(n-1)
print(s_2)
s = math.sqrt(s_2)
print(s)

gamma = 0.95
t_gamma = sts.t.ppf((1+gamma)/2, n-1)
print(t_gamma)
s_e = s/math.sqrt(n)
delta = t_gamma*s_e
print(x_sr -delta, x_sr+delta)

print(sts.t.interval(gamma, n - 1, x_sr, s_e))

# Данные
n = 52                 # количество недель
x_sr = 0.007          # выборочная средняя
s = 0.04               # выборочное стандартное отклонение
gamma = 0.95           # уровень значимости для 95% доверительного интервала

# 1. Доверительный интервал
df = n - 1  # степени свободы
t_gamma = sts.t.ppf((1+gamma)/2, n-1)  # критическое значение t
s_e = s / np.sqrt(n)  # стандартная ошибка
delta = t_gamma * s_e     # полуширина интервала

ci_lower = x_sr - delta
ci_upper = x_sr + delta

print(f"0.95-доверительный интервал: [{ci_lower:.4f}, {ci_upper:.4f}]")

# 2. Вероятность, что средняя доходность >= 0
z = (0 - x_sr) / (s / np.sqrt(n))
prob_positive = 1 - sts.norm.cdf(z)

print(f"Вероятность, что средняя недельная доходность >= 0: {prob_positive:.4f}")
