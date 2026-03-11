import time
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from scipy import stats


# Алгоритм проверки двудольности

def is_bipartite(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    color = [-1] * n
    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            while queue:
                v = queue.popleft()
                for neighbor in graph[v]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[v]
                        queue.append(neighbor)
                    elif color[neighbor] == color[v]:
                        return False
    return True


# Генерация случайного графа

def random_graph(n, p=0.3):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                edges.append((i,j))
    return edges


# Параметры эксперимента

ns = [10, 20, 50, 100, 200]  # размеры графов
trials = 100                  # число экспериментов на каждый n
p = 0.3                        # вероятность появления ребра

mean_times = []
std_times = []


# Измеряем время для разных n

for n in ns:
    times = []
    for _ in range(trials):
        edges = random_graph(n, p)
        start = time.time()
        is_bipartite(n, edges)
        end = time.time()
        times.append(end - start)
    times = np.array(times)
    mean_times.append(np.mean(times))
    std_times.append(np.std(times))
    if n == 50:  # сохраняем для гистограммы и проверки распределения
        times_n50 = times


# График времени vs n с погрешностью ±2 СКО

plt.figure(figsize=(8,5))
plt.errorbar(ns, mean_times, yerr=[2*s for s in std_times], fmt='-o', capsize=5)
plt.xlabel("Размер графа n")
plt.ylabel("Время решения (сек)")
plt.title("Зависимость времени решения от размера графа")
plt.grid(True)
plt.show()


# Гистограмма времени для n=50

plt.figure(figsize=(8,5))
plt.hist(times_n50, bins=10, edgecolor='black')
plt.xlabel("Время решения (сек)")
plt.ylabel("Количество экспериментов")
plt.title("Гистограмма времени для n=50")
plt.grid(True)
plt.show()


# Проверка нормальности распределения времени

k2, p_value = stats.normaltest(times_n50)
print(f"p-value для нормальности (n=50): {p_value:.4f}")
if p_value > 0.05:
    print("Гипотеза о нормальном распределении времени не отвергается")
else:
    print("Гипотеза о нормальном распределении времени отвергается")


# Вывод статистики

print("\nСреднее время и СКО для разных n:")
for i, n in enumerate(ns):
    print(f"n={n}: среднее={mean_times[i]:.6f} с, СКО={std_times[i]:.6f} с")
