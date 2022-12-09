data = open("input2.txt").read().splitlines()
arr = {'X': 1, 'Y': 2, 'Z':3}
mp = {'A':'Z', 'B': 'X', 'C': 'Y'}
wn = {'A':'Y', 'B':'Z', 'C':'X'}
eq = {'A':'X', 'B': 'Y', 'C':'Z'}
total = 0
for i in range(len(data)):
    val = data[i]
    opp = val[0]
    me = val[2]
    if me == 'X':
        total += arr[mp[opp]] + 0
    elif me == 'Y':
        total += arr[eq[opp]] + 3
    else:
        total += arr[wn[opp]] + 6
print(total)
