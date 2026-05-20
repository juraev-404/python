def find(p, x):
    while p[x] != x:
        x = p[x]
    return x


def union(p, a, b):

    a = find(p, a)
    b = find(p, b)

    if a == b:
        return False

    p[b] = a
    return True

def kruskal(n, edges, first_type):

    # first_type = 'A' или 'B'
    edges.sort(key=lambda e: e[2] != first_type)

    p = list(range(n))

    count_A = 0
    tree = []

    for u, v, t in edges:

        if union(p, u, v):

            tree.append((u, v, t))

            if t == 'A':
                count_A += 1

    if len(tree) != n - 1:
        return None, None

    return tree, count_A


def solve(n, edges, k):

    # минимум A
    _, mn = kruskal(n, edges[:], 'B')

    # максимум A
    _, mx = kruskal(n, edges[:], 'A')

    if k < mn or k > mx:
        print("Решения нет")
        return

    # строим ответ
    p = list(range(n))

    ans = []
    cnt = 0

    # сначала добавляем A
    for u, v, t in edges:

        if t == 'A' and cnt < k:

            if union(p, u, v):
                ans.append((u, v, t))
                cnt += 1

    # потом любые
    for u, v, t in edges:

        if union(p, u, v):
            ans.append((u, v, t))

    if len(ans) != n - 1:
        print("Решения нет")
        return

    print("Ответ:")
    for e in ans:
        print(e)


# ------------------------

n = 5

edges = [
    (0, 1, 'A'),
    (0, 2, 'B'),
    (1, 2, 'A'),
    (1, 3, 'B'),
    (2, 3, 'A'),
    (3, 4, 'B')
]

k = 2

solve(n, edges, k)