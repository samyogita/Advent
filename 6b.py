data = open('input6.txt').read()
l = 0
char = set()
print(data)
for r in range(len(data)):
    while data[r] in char:
        char.remove(data[l])
        l += 1
    char.add(data[r])
    if len(char) == 14:
        print(r+1)
        break

