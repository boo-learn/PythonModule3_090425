# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


from Lesson08.examples.dfs import visited

graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

def dfs(graph: list[list], start_vertex: int) -> list[bool]:
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * len(graph)
    _dfs(start_vertex)
    return visited

visited = dfs(graph, 1)
print(visited)
start_nodes = [8, 13, 3, 5]
key1 = 10
key2 = 7
target = 0

lock1 = (4, 5)
lock2 = (14, 15)

def unlock(graph, a, b):
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

lock1_opened = False
lock2_opened = False

for start in start_nodes.copy():
    visited = dfs(graph, start)
    if visited[target]:
        print(f"Цель ({target}) достижима из вершины s - {start}.")
        start_nodes.remove(start)

for start in start_nodes:
    visited = dfs(graph, start)
    if not lock1_opened and visited[key1]:
        unlock(graph, *lock1)
        lock1_opened = True
        print(f" Для s - {start} ключ  ({key1}) найден. Замок {lock1} открыт.")
        print(f"Цель ({target}) достижима из вершины s - {start}.")

    elif not lock2_opened and visited[key2]:
        unlock(graph,*lock2)
        lock2_opened = True
        print(f" Для s - {start} ключ  ({key2}) найден. Замок {lock2} открыт.")
        print(f"Но цель ({target}) недостижима для этой вершины.")
    else:
        print(f" Для s - {start} ключ не найден.")
        print(f"и цель ({target}) недостижима для этой вершины.")

#Vladimir Ghilas
