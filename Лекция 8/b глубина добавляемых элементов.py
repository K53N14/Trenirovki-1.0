def createnode(value, root, lvl):
    if value == root['value']:
        return 0
    if value < root['value']:
        if root['left'] == None:
            node = {'value': value, 'left': None, 'right': None}
            root['left'] = node
            lvl += 1
            return lvl
        else:
            lvl += 1
            lvl = createnode(value, root['left'], lvl)
            return lvl
    elif value > root['value']:
        if root['right'] == None:
            node = {'value': value, 'left': None, 'right': None}
            root['right'] = node
            lvl += 1
            return lvl
        else:
            lvl += 1
            lvl = createnode(value, root['right'], lvl)
            return lvl


seq = list(map(int, input().split()))
if len(seq) == 1:
    print(0)
else:
    root = {'value':seq[0], 'left': None, 'right': None}
    ans = []
    ans.append(1)
    for i in range(1, len(seq) - 1):
        lvl = createnode(seq[i], root, 1)
        if lvl != 0:
            ans.append(lvl)
print(*ans)