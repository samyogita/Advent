data = open('input5.txt').read()
crates , instr = data.split('\n\n')
crates = crates.splitlines()
crates.pop()
for i in range(len(crates)):
    crates[i] = crates[i][1::4]
crates = list(zip(*crates[::-1]))
crates = [[x for x in cur if x != ' '] for cur in crates]
instr = instr.splitlines()
moves = [[int(x) for x in move.split() if x.isdigit()] for move in instr]
for i in range(len(moves)):
    m = moves[i][0]
    f = moves[i][1] - 1
    t = moves[i][2] - 1
    for j in crates[f][-m:]:
        crates[t].append(j)
    crates[f] = crates[f][:-m]
print(''.join(x[-1] for x in crates))

