s = input()

num = int(s[0])
for i in range(1, len(s)):
    # if num == 0 or int(s[i]) == 0: num += int(s[i])
    # elif num == 1 or int(s[i]) == 1: num += int(s[i])
    if num <= 1 or int(s[i]) <= 1: num += int(s[i])
    else: num *= int(s[i])

print(num)
    