data = open('input10.txt').read().splitlines()
res = [1]
total = 0
for line in data:
    line = line.split()
    if line[0] == 'noop':
        res.append(0)
        continue
    res.append(0)
    res.append(int(line[1]))
total = 20 * sum(res[:20]) + 60 * sum(res[:60]) + 100 * sum(res[:100]) + 140 * sum(res[:140]) + 180 * sum(res[:180]) + 220 * sum(res[:220])
print(total)