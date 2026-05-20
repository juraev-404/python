# Крускал с возможностью получать разные MST
# за счет разного порядка ребер одинакового веса


parent = {}
rank = {}


# DSU

def make_set(vertices):

    for v in vertices:
        parent[v] = v
        rank[v] = 0


def find(v):

    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]


def union(a, b):

    a = find(a)
    b = find(b)

    if a != b:

        if rank[a] < rank[b]:
            a, b = b, a

        parent[b] = a

        if rank[a] == rank[b]:
            rank[a] += 1


# Крускал
def kruskal(vertices, edges):

    make_set(vertices)

    mst = []
    total = 0

    for u, v, w in edges:

        if find(u) != find(v):

            union(u, v)

            mst.append((u, v, w))
            total += w

    return mst, total


# пример
vertices = [0, 1, 2, 3]

# ребра:
# (u, v, weight)

edges1 = [
    (0, 1, 1),
    (1, 2, 1),
    (0, 2, 1),   # одинаковый вес
    (2, 3, 2)
]

# другой порядок ребер одинакового веса

edges2 = [
    (0, 2, 1),
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 2)
]


mst1, cost1 = kruskal(vertices, edges1)

mst2, cost2 = kruskal(vertices, edges2)


print("MST 1:")
for e in mst1:
    print(e)

print("Стоимость:", cost1)

print()

print("MST 2:")
for e in mst2:
    print(e)

print("Стоимость:", cost2)