data = open("input1.txt").read().splitlines()
res = []
total = 0
mx = 0
length = len(data)
for i in range(len(data)):
    if data[i] == '':
        res.append(total)
        total = 0
    else:
        total += int(data[i])
res.append(total)
res = sorted(res)
mx = res[-1]+ res[-2]+ res[-3]
print(mx)

