graph = [
    [1, 4],  # 0
    [0, 2],  # 1
    [1],  # 2
    [7],  # 3
    [0],  # 4
    [6,9],  # 5
    [5, 10],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [5,8, 10],  # 9
    [6, 9, 14],  # 10
    [7],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]
treasures = {
    1: 1,
    2: 2,
    4: 3,
    6: 5,
    7: 3,
    9: 5,
    10: 3,
    13: 8,
    14: 4,
    15: 7
}

start_nodes = {
    "S-1": 0,
    "S-2": 3,
    "S-3": 12
}

# Решите задачу и выведите ответ в нужном формате
def dfs(graph: list[list], start_vertex: int) -> list[bool]:
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * len(graph)
    _dfs(start_vertex)
    return visited

def dfs_collect_treasures(graph: list[list], start: int, treasures: dict[int, int]) -> int:
    visited = dfs(graph, start)
    total = 0
    for v in range(len(graph)):
        if visited[v] and v in treasures:
            total += treasures[v]
    return total

visited = dfs(graph, 0)
print(visited)

for label, node in start_nodes.items():
    value = dfs_collect_treasures(graph, node, treasures)
    print(f"Из точки {label} можно собрать сокровищ суммарной ценностью {value}")

#Vladimir Ghilas
