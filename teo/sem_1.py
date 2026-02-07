import numpy as np
from scipy.stats import binom, norm
import math

# параметры
n = 500
p = 0.54
a = 5500   # мат. ожидание чека
sigma = 80 # стандартное отклонение чека

# характеристики X (число покупателей)
E_X = binom.mean(n, p)         # E[X] = np
print(E_X)
Var_X = binom.var(n, p)        # Var[X] = np(1-p)
print(Var_X)

# характеристики Y (сумма чека одного покупателя)
E_Yi = a                       # E[Y_i] = a
print(E_Yi)
Var_Yi = sigma**2              # Var[Y_i] = sigma^2
print(Var_Yi)
# итоговая выручка R = sum_{i=1}^X Y_i
E_R = E_X * E_Yi
Var_R = Var_Yi * E_X + (E_Yi**2) * Var_X
Sigma_R = math.sqrt(Var_R)

print("E[R] =", E_R)
print("Var(R) =", Var_R)
print("sigma(R) =", Sigma_R)



# параметры
n = 500
p = 0.54
a = 5500
sigma = 80

N = 10**5  # сколько "дней" моделируем

# 1) число покупателей X в каждый день
X = np.random.binomial(n, p, N)

# 2) считаем выручку Z[i] для каждого дня
Z = np.zeros(N)
for i in range(N):
    # генерируем X[i] чеков по нормальному распределению
    Y = np.random.normal(a, sigma, X[i])
    Z[i] = np.sum(Y)

# оценки методом Монте-Карло
E_Y = np.mean(Z)   # средняя выручка
Var_Y = np.var(Z)  # дисперсия выручки
Sigma_Y = np.std(Z)

print("Monte Carlo E[Y] =", E_Y)
print("Monte Carlo Var(Y) =", Var_Y)
print("Monte Carlo sigma(Y) =", Sigma_Y)
