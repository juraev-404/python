import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# алгоритм максимального независимого множества
def max_independent_set(n, edges):

    graph = [set() for _ in range(n)]

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    best_set = []

    def backtrack(current_set, candidates):

        nonlocal best_set

        if len(current_set) > len(best_set):
            best_set = current_set[:]

        for v in list(candidates):

            new_candidates = candidates - graph[v] - {v}

            backtrack(current_set + [v], new_candidates)

            candidates.remove(v)

    backtrack([], set(range(n)))

    return best_set


# генерация случайного графа
def random_graph(n, p=0.3):

    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                edges.append((i, j))

    return edges


# параметры эксперимента

ns = [6,7,8,9,10,11]     # размеры графов
trials = 50              # число экспериментов
p = 0.3                  # вероятность ребра

mean_times = []
std_times = []

# измерение времени

for n in ns:

    times = []

    for _ in range(trials):

        edges = random_graph(n, p)

        start = time.time()
        max_independent_set(n, edges)
        end = time.time()

        times.append(end - start)

    times = np.array(times)

    mean_times.append(np.mean(times))
    std_times.append(np.std(times))

    if n == 9:
        times_for_hist = times


# график зависимости времени от n

plt.figure()

plt.errorbar(
    ns,
    mean_times,
    yerr=[2*s for s in std_times],
    marker='o'
)

plt.xlabel("Размер графа n")
plt.ylabel("Время работы (сек)")
plt.title("Зависимость времени решения от размера графа")

plt.grid(True)
plt.show()


# гистограмма времени

plt.figure()

plt.hist(times_for_hist, bins=10)

plt.xlabel("Время решения (сек)")
plt.ylabel("Количество экспериментов")
plt.title("Гистограмма времени для n=9")

plt.show()


# проверка гипотезы о нормальности

k2, p_value = stats.normaltest(times_for_hist)

print("p-value =", p_value)

if p_value > 0.05:
    print("Гипотеза о нормальном распределении не отвергается")
else:
    print("Гипотеза о нормальном распределении отвергается")


# вывод статистики

print("\nСреднее время и СКО:")

for i, n in enumerate(ns):

    print(
        "n =", n,
        "  mean =", round(mean_times[i],6),
        "  std =", round(std_times[i],6)
    )
