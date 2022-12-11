data = open("input4.txt").read().splitlines()
count = 0
for i in data:
    f, s = i.split(',')
    a,b = f.split('-')
    c,d = s.split('-')
    if int(a) > int(d) or int(b) < int(c):
        continue
    else:
        count += 1
print(count)
    

