s = input()

num = []
char = []

for c in s:
    try: 
        n = int(c)
        num.append(n)
    except: 
        char.append(c)

print(''.join(sorted(char)) + str(sum(num)))