data = open('input8.txt').read().splitlines()
m = len(data)
n = len(data[0])
count = 0
for i in range(m):
    for j in range(n):
        up = down = left = right = True
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            count += 1
            continue
        for k in range(j-1,-1,-1):
            if data[i][k] >= data[i][j]:
                left = False
        for k in range(i-1,-1,-1):
            if data[k][j] >= data[i][j]:
                up = False
        for k in range(i+1,m):
            if data[k][j] >= data[i][j]:
                down = False
        for k in range(j+1,n):
            if data[i][k] >= data[i][j]:
                right = False
        if left or right or up or down:
            count += 1
print(count)