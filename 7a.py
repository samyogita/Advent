from collections import defaultdict
data = open('input7.txt').read().splitlines()
st = []
size = defaultdict(int)
g = defaultdict(list)

def dfs(parent):
    for child in g[parent]:
        size[parent] += dfs(child)
    return size[parent]

for cmd in data:
    cmd = cmd.split()
    if '$' in cmd:
        if 'ls' in cmd:
            continue
        elif 'cd' in cmd:
            if '..' in cmd:
                st.pop()
            else:
                st.append(cmd[-1])
    else:
        if cmd[0] == 'dir':
            cur = '/'.join(st)
            g[cur].append(cur + '/' + cmd[-1])
        else:
            cur = '/'.join(st)
            size[cur] += int(cmd[0])
print(size)
dfs('/')
ans = 0
for val in size.values():
    if val < 100000:
        ans += val

print(size,ans)

