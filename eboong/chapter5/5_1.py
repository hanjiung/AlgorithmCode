row, col = map(int, input().split())
graph = []
for k in range(row):
    graph.append(list(map(int,input())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= row or y >= col:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(row):
    for j in range(col):
        if dfs(i, j) == True:
            result += 1
    # visited[v] = True
    # print(v, end=' ')
    # for i in graph[v]:
    #     if not visited[i]:
    #         dfs(graph, i, visited)

print(result)
