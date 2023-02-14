def createnode(value, root):
    if value < root['value']:
        if root['left'] == None:
            node = {'value': value, 'left': None, 'right': None}
            root['left'] = node
        else:
            createnode(value, root['left'])
    elif value > root['value']:
        if root['right'] == None:
            node = {'value': value, 'left': None, 'right': None}
            root['right'] = node
        else:
            createnode(value, root['right'])

def printtree(root, ans):
    if root['left'] != None:
        printtree(root['left'], ans)
        ans.append(root['value'])
        if root['right'] != None:
            printtree(root['right'], ans)
        else:
            return(ans)
    elif root['right'] != None:
        ans.append(root['value'])
        printtree(root['right'], ans)

    else:
        return(ans.append(root['value']))

    return (ans)

seq = list(map(int, input().split()))
root = {'value':seq[0], 'left': None, 'right': None}

for i in range(1, len(seq) - 1):
    createnode(seq[i], root)
ans = []
ans = printtree(root, ans)
print('\n'.join(map(str, ans)))