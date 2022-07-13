def mapping(c):
    if c == 'a':
        return 1
    elif c == 'b':
        return 2
    elif c == 'c':
        return 3
    elif c == 'd':
        return 4
    elif c == 'e':
        return 5
    elif c == 'f':
        return 6
    elif c == 'g':
        return 7
    elif c == 'h':
        return 8
    
loc = input()

x = mapping(loc[0])
y = int(loc[1])
count = 0
dir = [(2,0), (-2,0), (0,2), (0,-2)]

for i in range(4):
    d = -1
    for j in range(2):
        if i < 2:
            dir2 = (0,d)
        else:
            dir2 = (d,0)
        nx = x + dir[i][0] + dir2[0]
        ny = y + dir[i][1] + dir2[1]
        if nx >= 1 and nx<=8 and ny >= 1 and ny <= 8: count += 1
        d *= -1
        
print(count)