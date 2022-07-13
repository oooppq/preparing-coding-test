n, m = map(int, input().split(' '))

l = []

for _ in range(n):
    l.append(list(map(int,input())))
# l = [[0] * m] * n
# for i in range(n):

for i in range(n):
    for j in range(m):
        l[i][j] = int(l[i][j])
# n = 4; m = 5
l = [[0,0,1,1,0],
     [0,0,0,1,1],
     [1,1,1,1,1],
     [0,0,0,0,0]]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j, l):
    l[i][j] = 1
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if ni >= 0 and ni < n and nj >= 0 and nj < m and l[ni][nj] == 0:
            dfs(ni, nj, l)
    
count = 0

for i in range(4):
    for j in range(5):
        if l[i][j] == 0:
            dfs(i, j, l)
            count += 1

print(count)
    