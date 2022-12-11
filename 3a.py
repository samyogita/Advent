data = open("input3.txt").read().splitlines()
sum = 0
for val in data:
    l = len(val) // 2
    flag = False
    for i in range(l):
        for j in range(l, len(val)):
            if val[i] == val[j]:
                x = val[i]
                flag = True
                break
        if flag:
            break
    if ord(x) >= ord('a'):
        sum += ord(x) - ord('a') + 1
    else:
        sum += ord(x) - ord('A') + 27
print(sum)

    
