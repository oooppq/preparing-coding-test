n = int(input())
l = sorted(map(int, input().split(' ')))

# 내 생각
# i = -1

# start = n
# count = 0
# while True:
#     i += l[start - 1]
#     if i > start: break
#     else: count+= 1
#     start -= 1
# print(count)

count = 0
now = 0
for i in l:
    now += 1
    if i <= now:
        count += 1
        now = 0

print(count)