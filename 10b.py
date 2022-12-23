data = open('input10.txt').read().splitlines()
A = [1]
res = ['' for k in range(6)]
total = 0
for line in data:
    line = line.split()
    if line[0] == 'noop':
        A.append(0)
        continue
    A.append(0)
    A.append(int(line[1]))
for i in range(0, 240, 40):
    for j in range(40):
        pos = sum(A[:i+j+1])

        if pos in (j-1, j, j+1):
            res[i // 40] += '#'
        else:
            res[i // 40] += '.'
for ele in res:
    print(ele , end = '\n')
