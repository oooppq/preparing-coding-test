from collections import deque

q = deque()

n, m = map(int, input().split(' '))

l = []

for _ in range(n):
    l.append(list(map(int,input())))

# 내가 짠 것
# def bfs(i, j, count, q):
#     q.append((i, j, count))
#     while q:
#         x, y, c = q.popleft()
#         if x >= 0 and y >= 0 and x < n and y < m and l[x][y] == 1: 
#             if x == n - 1 and y == m - 1: 
#                 print(c)
#                 return
#             l[x][y] = 0
#             q.append((x + 1, y, c + 1))
#             q.append((x - 1, y, c + 1))
#             q.append((x, y + 1, c + 1))
#             q.append((x, y - 1, c + 1))

# bfs(0, 0, 1, q)
            
# 정석

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q.append((i, j))
    while q:
        popi, popj = q.popleft()
        if popi == n - 1 and popj == m - 1: print(l[popi][popj])
        for k in range(4):
            ni = popi + dx[k]        
            nj = popj + dy[k]
            if ni >= 0 and nj >= 0 and ni < n and nj < m and l[ni][nj] == 1:
                l[ni][nj] = l[popi][popj] + 1
                q.append((ni, nj))


bfs(0,0)
