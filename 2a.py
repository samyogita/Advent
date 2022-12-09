data = open("input2.txt").read().splitlines()
arr = {'X': 1, 'Y': 2, 'Z':3}
mp = {'A' : 'Y', 'B': 'Z', 'C': 'X'}
eq = {'A':'X', 'B': 'Y', 'C':'Z'}
total = 0
for i in range(len(data)):
    val = data[i]
    opp = val[0]
    me = val[2]
    if mp[opp] == me:
        total += arr[me] + 6
    elif eq[opp] == me:
        total += arr[me] + 3
    else:
        total += arr[me] + 0
print(total)

