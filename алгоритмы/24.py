graph = {}

def add_edge(u, v, w):

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append((v, w))
    graph[v].append((u, w))


# поиск максимального ребра на пути
def dfs(current, target, visited, max_weight):

    if current == target:
        return max_weight

    visited.add(current)

    for neighbor, weight in graph[current]:

        if neighbor not in visited:

            result = dfs(
                neighbor,
                target,
                visited,
                max(max_weight, weight)
            )

            if result != -1:
                return result

    return -1


# (a) Проверка MST
def check_mst(u, v, new_weight):

    max_edge = dfs(u, v, set(), -1)

    if new_weight >= max_edge:
        print("Старое MST остается минимальным")
    else:
        print("Старое MST больше не минимально")


# (b) Обновление MST
def update_mst(u, v, new_weight):

    visited = set()
    parent = {}

    # поиск пути
    def find_path(cur, target):

        if cur == target:
            return True

        visited.add(cur)

        for nei, w in graph[cur]:

            if nei not in visited:

                parent[nei] = (cur, w)

                if find_path(nei, target):
                    return True

        return False

    find_path(u, v)

    # ищем максимальное ребро на пути
    current = v

    max_w = -1
    remove_u = -1
    remove_v = -1

    while current != u:

        prev, w = parent[current]

        if w > max_w:
            max_w = w
            remove_u = prev
            remove_v = current

        current = prev

    if new_weight >= max_w:
        print("MST менять не нужно")
        return

    # удаляем тяжелое ребро
    graph[remove_u] = [
        (x, w) for x, w in graph[remove_u]
        if x != remove_v
    ]

    graph[remove_v] = [
        (x, w) for x, w in graph[remove_v]
        if x != remove_u
    ]

    # добавляем новое ребро
    add_edge(u, v, new_weight)

    print("MST обновлено")
    print("Удалено ребро:", remove_u, "-", remove_v)
    print("Добавлено ребро:", u, "-", v)


# вывод дерева
def show():
    used = set()
    for u in graph:
        for v, w in graph[u]:
            if (v, u) not in used:
                print(u, "-", v, "=", w)
                used.add((u, v))



add_edge(0, 1, 2)
add_edge(1, 2, 3)
add_edge(1, 3, 5)
add_edge(3, 4, 6)

print("Исходное MST:")
show()

print("(a) Проверка")

check_mst(2, 4, 4)

print("(b) Обновление")

update_mst(2, 4, 4)

print("Новое MST:")
show()