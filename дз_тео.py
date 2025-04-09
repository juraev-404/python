import itertools
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# 6.1

# Возможные значения X
domain = [1, 2, 3, 4, 5]
prob = [0.2] * 5  # Равномерное распределение

# Генерация всех возможных троек (X1, X2, X3)
all_combinations = list(itertools.product(domain, repeat=3))

# Вычисляем max(X1, X2, X3) для каждой тройки
max_values = [max(x) for x in all_combinations]

# Вычисляем вероятности для каждого значения Y
y_values, counts = np.unique(max_values, return_counts=True)
y_probs = counts / len(all_combinations)

# Вывод распределения Y
print('#6.1: ')
for y, p in zip(y_values, y_probs):
    print(f"P(Y = {y}) = {p:.4f}")


# 6.3

# 1. Определяем распределения X, Y, Z
X_values = np.arange(0, 13)
X_probs = np.full_like(X_values, 1/13, dtype=float)

Y_values = np.arange(0, 14)
Y_probs = np.full_like(Y_values, 1/14, dtype=float)
Y_probs[3] = 9/10
Y_probs /= Y_probs.sum()

Z_values = np.array([3, 7])
Z_probs = np.array([0.5, 0.5])

# 2. Генерируем выборки
num_samples = 500000
X_sample = np.random.choice(X_values, size=num_samples, p=X_probs)
Y_sample = np.random.choice(Y_values, size=num_samples, p=Y_probs)
Z_sample = np.random.choice(Z_values, size=num_samples, p=Z_probs)

# 3. Вычисляем сумму
sum_samples = X_sample + Y_sample + Z_sample

# 4. Вероятность P(X + Y + Z = 12)
prob_12 = np.sum(sum_samples == 12) / num_samples
print('#6.3')
print(f"a) P(X + Y + Z = 12) ≈ {prob_12:.4f}")

# 5. График относительной частоты
exp_counts = np.arange(100, num_samples, step=1000)  # Увеличен диапазон
relative_frequencies = [np.sum(sum_samples[:count] == 12) / count for count in exp_counts]

plt.figure(figsize=(10, 4))
plt.plot(exp_counts, relative_frequencies, 'b-', alpha=0.7)
plt.axhline(y=prob_12, color='r', linestyle='--', label=f"Теоретическая P = {prob_12:.4f}")
plt.xlabel("Число экспериментов")
plt.ylabel("Относительная частота P(X + Y + Z = 12)")
plt.title("Сходимость относительной частоты к вероятности")
plt.legend()
plt.grid()
plt.show()

# 6. Распределение суммы X + Y + Z
sum_distribution = Counter(sum_samples)
total_count = sum(sum_distribution.values())

values = sorted(sum_distribution.keys())
probabilities = [sum_distribution[v] / total_count for v in values]

# Вывод вероятности для M = 16
M = 16
prob_M = sum_distribution[M] / total_count if M in sum_distribution else 0
print(f"b) P(X + Y + Z = {M}) ≈ {prob_M:.4f}")

plt.figure(figsize=(8, 4))
plt.bar(values, probabilities, color='red', alpha=0.6, label="P(X+Y+Z)")
plt.scatter(values, probabilities, color='blue', s=10)
plt.axhline(y=prob_M, color='green', linestyle='-', label=f"P(M={M}) = {prob_M:.4f}")
plt.xlabel("Значение суммы")
plt.ylabel("Вероятность")
plt.title("Распределение суммы X + Y + Z")
plt.legend()
plt.grid()
plt.show()


# 6.4

# 1. Определяем распределения X, Y, Z
X_values = np.arange(1, 16)
X_probs = np.full_like(X_values, 1/15, dtype=float)

Y_values = np.arange(1, 13)
Y_probs = np.full_like(Y_values, 1/12, dtype=float)

Z_values = np.arange(1, 12)
Z_probs = np.full_like(Z_values, 1/11, dtype=float)

# 2. Генерируем выборки
num_samples = 500000 
X_sample = np.random.choice(X_values, size=num_samples, p=X_probs)
Y_sample = np.random.choice(Y_values, size=num_samples, p=Y_probs)
Z_sample = np.random.choice(Z_values, size=num_samples, p=Z_probs)

# 3. Вычисляем вероятности P(X < Y < Z)
prob_X_Y_Z = np.sum((X_sample < Y_sample) & (Y_sample < Z_sample)) / num_samples
print('#6.4: ')
print(f"a) P(X < Y < Z) ≈ {prob_X_Y_Z:.4f}")

# 4. Вычисляем вероятность P(2X < Y < 2Z)
prob_2X_Y_2Z = np.sum((2 * X_sample < Y_sample) & (Y_sample < 2 * Z_sample)) / num_samples
print(f"b) P(2X < Y < 2Z) ≈ {prob_2X_Y_2Z:.4f}")

# 5. График
exp_counts = np.arange(100, num_samples, step=1000)
relative_frequencies = [np.sum((2 * X_sample[:count] < Y_sample[:count]) & (Y_sample[:count] < 2 * Z_sample[:count])) / count for count in exp_counts]

plt.figure(figsize=(10, 4))
plt.plot(exp_counts, relative_frequencies, 'b-', alpha=0.7)
plt.axhline(y=prob_2X_Y_2Z, color='r', linestyle='--', label=f"Теоретическая P = {prob_2X_Y_2Z:.4f}")
plt.xlabel("Число экспериментов")
plt.ylabel("Относительная частота P(2X < Y < 2Z)")
plt.title("Сходимость относительной частоты к вероятности")
plt.legend()
plt.grid()
plt.show()


# 6.8

num_vars = 40  # Количество X_i
prob_X_positive = 0.98  # Вероятность P(X_i > 0)
prob_product_positive = prob_X_positive ** num_vars  # P(X_1 * X_2 * ... * X_40 > 0)
print('#6.8: ')
print(f"P(X_1 * X_2 * ... * X_40 > 0) ≈ {prob_product_positive:.6f}")

# 7. График
num_trials = np.arange(100, num_samples, 1000)
positive_counts = [np.prod(np.random.choice([1, -1], size=(count, num_vars), p=[prob_X_positive, 1 - prob_X_positive]), axis=1) > 0 for count in num_trials]
relative_frequencies_6_8 = [np.mean(counts) for counts in positive_counts]

plt.figure(figsize=(10, 4))
plt.plot(num_trials, relative_frequencies_6_8, 'g-', alpha=0.7)
plt.axhline(y=prob_product_positive, color='r', linestyle='--', label=f"Теоретическая P = {prob_product_positive:.6f}")
plt.xlabel("Число экспериментов")
plt.ylabel("Относительная частота P(X_1 * ... * X_40 > 0)")
plt.title("Сходимость относительной частоты к вероятности")
plt.legend()
plt.grid()
plt.show()


