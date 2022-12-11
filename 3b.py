data = open("input3.txt").read().splitlines()
sum = 0
for i in range(0, len(data), 3):
    a = set(data[i])
    b = set(data[i+1])
    c = set(data[i+2])
    x = a.intersection(b).intersection(c)
    val = max(x)
    if ord(val) >= ord('a'):
        sum += ord(val) - ord('a') + 1
    else:
        sum += ord(val) - ord('A') + 27
print(sum)