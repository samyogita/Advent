data = open("input4.txt").read().splitlines()
count = 0
for i in data:
    f, s = i.split(',')
    a,b = f.split('-')
    c,d = s.split('-')
    if int(a) <= int(c) and int(b) >= int(d):
        count += 1
    elif int(a) >= int(c) and int(b) <= int(d):
        count += 1
print(count)
    

