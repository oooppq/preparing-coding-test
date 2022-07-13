dir = [(0,1), (1,0), (0,-1), (-1,0)]

n = int(input())

l = input().split(' ')

def dir_check(d):
    if d == 'R': return dir[0]
    elif d == 'D': return dir[1]
    elif d == 'L': return dir[2] 
    elif d == 'U': return dir[3]

def avail_check(x, y, n):
    if x < 1 or y < 1 or x > n or y > n: return False
    return True

now = [1,1]

for d in l:
    to = dir_check(d)
    moved = [now[0] + to[0], now[1] + to[1]]
    if avail_check(moved[0], moved[1], n):
        now = moved

print(now[0], now[1])
    