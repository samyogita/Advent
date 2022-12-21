data = open('input8.txt').read().splitlines()
m = len(data)
n = len(data[0])
res = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        up = down = left = right = 0
        for k in range(j-1,-1,-1):
            left += 1
            if data[i][k] >= data[i][j]:
                break   
        for k in range(i-1,-1,-1):
            up += 1
            if data[k][j] >= data[i][j]:
                break
        for k in range(i+1,m):
            down += 1
            if data[k][j] >= data[i][j]:
                break
        for k in range(j+1,n):
            right += 1
            if data[i][k] >= data[i][j]:
                break
        res = max(res, left*up*down*right)
print(res)