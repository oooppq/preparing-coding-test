# #1트
# l = map(int, input().split(' '))

# for i in l:
#     lenI = len(str(i))
#     while True:
#         num = int('1' * lenI)
#         if (num % i) == 0:
#             print(lenI)
#             break
#         else: lenI += 1
        
#2트 그냥 입력 방식때문에 틀린거였음;;
while True:
    try: n = int(input())
    except: break
    
    lenI = len(str(n))
    while True:
        num = int('1' * lenI)
        if (num % n) == 0:
            print(lenI)
            break
        else: lenI += 1

    
