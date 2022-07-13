# 17427과 똑같이하면 시간초과, 방법 모르겠어서 구글링함ㅜㅜ
# num = int(input())
# for i in range(num):
#     n = int(input())
#     sum = 0
#     for i in range(1, n + 1):
#         sum += (n // i) * i
#     print(sum)

import sys

sum = [1] * 1000001
cumm = [0] * 1000001

for i in range(2, 1000001):
    j = 1
    while i * j <= 1000000:
        sum[i * j] += i
        j += 1

for i in range(1, 1000001):
    cumm[i] = cumm[i - 1] + sum[i]
    
l = int(sys.stdin.readline())
for i in range(l):
    j = int(sys.stdin.readline())
    print(cumm[j])
    
# n = int(input())
# ans=[]
# for _ in range(n):
#     a=int(input())
#     ans.append(cumm[a])
# print('\n'.join(map(str, ans))+'\n')
    