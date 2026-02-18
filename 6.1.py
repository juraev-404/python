# import itertools
# import numpy as np
# from random import randint

# # Возможные значения X

# domain = [0,0,0,0,0,0,0,0,0,1,1,1]
# prob = [0.2] * 12  # Равномерное распределение
# li1 = []

# all_combinations = list(itertools.product(domain, repeat=4))
# for i in range(48):
#     for i in range(len(domain)):
#         li1.append(domain.pop(randint(0, len(domain))))
    
#     domain = [0,0,0,0,0,0,0,0,0,1,1,1]

# max_values = [sum(x) for x in all_combinations if sum(x)!=0 and sum(x)!=4]

# # Вычисляем вероятности для каждого значения Y
# y_values, counts = np.unique(max_values, return_counts=True)
# y_probs = counts / len(all_combinations)

# # Вывод распределения Y
# for y, p in zip(y_values, y_probs):
#     print(f"P(Y = {y}) = {p:.4f}")


import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(n)]

INF = 10**30
t = [[INF]*m for _ in range(n)]
pq = []

# стартовые точки — вся вода
for i in range(n):
    for j in range(m):
        if h[i][j] == 0:
            t[i][j] = 0
            heapq.heappush(pq, (0, i, j))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while pq:
    cur, x, y = heapq.heappop(pq)
    if cur != t[x][y]:
        continue

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            # вода идёт 1 минуту + уровень должен дойти до высоты
            new_t = max(cur + 1, h[nx][ny])
            if new_t < t[nx][ny]:
                t[nx][ny] = new_t
                heapq.heappush(pq, (new_t, nx, ny))

for row in t:
    print(*row)
