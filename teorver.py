import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# график для задания №2

# Интервал значений Y от 1 до e
y = np.linspace(1, np.e, 500)
# Плотность распределения: f_Y(y) = 1 / y
f_y = 1 / y

# Построение графика
plt.figure(figsize=(8, 5))
plt.plot(y, f_y, label=r'$f_Y(y) = \frac{1}{y}$', color='blue')
plt.title('Плотность распределения Y = e^X, где X ~ U[0,1]')
plt.xlabel('y')
plt.ylabel('f_Y(y)')
plt.grid(True)
plt.legend()
plt.show()



# задание №3

# Подынтегральная функция: y * f_Y(y) = y * (1/y) = 1
def integrand(y):
    return 1

# Интегрирование по интервалу [1, e]
expected_value, _ = integrate.quad(integrand, 1, np.e)

print(f"Математическое ожидание M[Y] = {expected_value}")



# задание №4

# Теоретическое значение
true_mean = np.e - 1

# Размеры выборки
sample_sizes = np.logspace(1, 5, num=10, dtype=int)
sample_means = []

# Генерация и расчет выборочных средних
for n in sample_sizes:
    X = np.random.uniform(0, 1, size=n)
    Y = np.exp(X)
    sample_means.append(np.mean(Y))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, sample_means, label='Выборочное среднее')
plt.axhline(true_mean, color='red', linestyle='--', label=r'$\mathbb{M}[Y] = e - 1$')
plt.xscale('log')
plt.xlabel('Размер выборки')
plt.ylabel('Среднее значение Y')
plt.title('Статистическая устойчивость M(Y)')
plt.legend()
plt.grid(True)
plt.show()
