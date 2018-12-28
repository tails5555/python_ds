N, E, S = input().split()
N = int(N)
E = int(E)
S = int(S)
graph = [ [0 for k in range(N+1)] for l in range(N+1) ]

for k in range(E) :
    x, y = input().split()
    x = int(x)
    y = int(y)
    graph[x][y] = graph[y][x] = 1

visited_dfs = set()

dfs_res = []

def dfs(idx) :
    if idx in visited_dfs :
        return
    visited_dfs.add(idx)
    dfs_res.append(idx)
    for (idx, k) in enumerate(graph[idx]) :
        if k == 1 and idx not in visited_dfs :
            dfs(idx)

dfs(S)

visited_bfs = set()
queue = []

visited_bfs.add(S)
queue.append(S)

bfs_res = ''
while len(queue) > 0 :
    tmp = queue.pop(0)
    bfs_res += '{} '.format(tmp)
    for (idx, k) in enumerate(graph[tmp]) :
        if k == 1 and idx not in visited_bfs :
            queue.append(idx)
            visited_bfs.add(idx)

result = ''
for s in dfs_res:
    result += str(s) + ' '

print(result.rstrip())
print(bfs_res)