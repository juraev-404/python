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
        for j in range(i + 1, n):
            if random.random() < p:
                edges.append((i, j))
    return edges


# Параметры эксперимента
random.seed(42)

ns = list(range(50, 601, 50))   # размеры графов
trials = 100                     # число экспериментов
repeats = 60                    # повторов внутри замера
p = 0.3

mean_times = []
std_times = []


# Измерение времени
for n in ns:
    times = []
    for _ in range(trials):
        edges = random_graph(n, p)

        start = time.perf_counter()
        for _ in range(repeats):
            is_bipartite(n, edges)
        end = time.perf_counter()

        times.append((end - start) / repeats)

    times = np.array(times)
    mean_times.append(np.mean(times))
    std_times.append(np.std(times))

    if n == 300:   # выбранное n для гистограммы
        times_selected = times


# График зависимости времени
plt.figure()
plt.errorbar(ns, mean_times, yerr=[2*s for s in std_times], fmt='-o')
plt.xlabel("Размер графа n")
plt.ylabel("Время (сек)")
plt.title("Зависимость времени от размера графа")
plt.grid()
plt.show()



mu = np.mean(times_selected)
sigma = np.std(times_selected)

x = np.linspace(min(times_selected), max(times_selected), 100)
y = stats.norm.pdf(x, mu, sigma)


plt.figure()
plt.hist(times_selected, bins=20, density=True, edgecolor='black')
plt.plot(x, y)
plt.xlabel("Время (сек)")
plt.ylabel("Плотность")
plt.title("Гистограмма времени (n=300)")
plt.grid()
plt.show()


# Проверка нормальности
k2, p_value = stats.normaltest(times_selected)

print(f"p-value: {p_value:.4f}")
if p_value > 0.05:
    print("Нормальность не отвергается")
else:
    print("Нормальность отвергается")


# Вывод статистики
print("\nСтатистика:")
for i, n in enumerate(ns):
    print(f"n={n}: среднее={mean_times[i]:.6f}, СКО={std_times[i]:.6f}")
