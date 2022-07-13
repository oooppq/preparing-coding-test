num = int(input())

l = list(map(int, input().split(' ')))

maxNum = 0
minNum = 1000001

if len(l) == 1: print(l[0] * l[0])
else:
    for i in l:
        if i > maxNum: maxNum = i
        if i < minNum: minNum = i
    print(maxNum * minNum)