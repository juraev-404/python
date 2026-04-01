import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


rank = [[m] * (n + 1) for _ in range(n)]

for i in range(n):
    for t in range(m):
        s = a[i][t]
        if s != 0 and rank[i][s] == m:
            rank[i][s] = t  


order = []
for i in range(n):
    stores = list(range(1, n + 1))
    stores.sort(key=lambda s: rank[i][s])
    order.append(stores)


store_pref = [[0] * n for _ in range(n + 1)]

for s in range(1, n + 1):
    trucks = list(range(n))
    trucks.sort(key=lambda i: rank[i][s])
    for pos, i in enumerate(trucks):
        store_pref[s][i] = pos


next_pos = [0] * n
match_store = [0] * n
match_truck = [-1] * (n + 1)

q = deque(range(n))

while q:
    v = q.popleft()
    s = order[v][next_pos[v]]
    next_pos[v] += 1

    u = match_truck[s]

    if u == -1 or store_pref[s][v] > store_pref[s][u]:
        match_truck[s] = v
        match_store[v] = s
        if u != -1:
            q.append(u)
    else:
        q.append(v)

print('\n'.join(map(str, match_store)))
