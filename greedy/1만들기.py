import time

start = time.time()
n, k = map(int, input().split(' '))
    
num = n
count = 0
while num != 1:
  if num % k == 0: num /= k
  else: num -= 1
  count += 1

print(count)
print(time.time() - start)


# 좀 더 빠른 방법임
# num = n
# count = 0

# while num != 1:
#     target = (num // k) * k
#     if target == 0: 
#         count += num - 1
#         break
#     count += num - target + 1
#     num = target // k

# print(count)