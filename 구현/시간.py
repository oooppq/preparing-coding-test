# 시: 받고
# 분: 5 * 1 +  1 * 10
# 초: 5 * 1 +  1 * 10

# 이렇게 하면 더 빠르긴 하지만 경우의 수가 많지 않아 굳이 이렇게 하지 않아도 돼
# n = int(input())

# count = 0

# for i in range(n+1):
#     if str(i)[-1] == '3': count += 3600
#     else: count += 15 * 60 + 15 * 60 - 15 * 15 
    
# print(count)

# 뭐 경우의 수가 많아지면 오래걸리겠지만 이 문제로는 충분해
n  = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): count += 1
print(count)