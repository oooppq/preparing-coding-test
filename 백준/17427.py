# # 접근방법을 아예 못찾아서 구글링함
# l = [0] * 1000001
# l[1] = 1; l[2] = 3; 
# check = [0] * 1000001
# check[1] = 1
# for i in (range(1, 1000001):
#     if check: continue
#     num = i
#     for j in range(2, int())
#     for j in range()
#     if i % 2:
#         # j = 1
#         # while True:
#         #     odd = j * 2 + 1
#         #     if i % odd == 0:
#         #         l[i] = l[odd] + i
#         #         if int(i / odd) != odd:
#         #             l[i] += int(i / odd)
#         #         break
#         #     j += 1
#         pass
#     else: 
#         l[i] = l[int(i/2)] + 2 + i

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += (n // i) * i
print(sum)
