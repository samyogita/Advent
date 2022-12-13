data = open('input6.txt').read()
l = 0
mp = {}
for r in range(len(data)):
    l = max(l, mp.get(data[r], -1) + 1)
    mp[data[r]] = r
    if r - l + 1 == 4:
        print(r+1)
        break


