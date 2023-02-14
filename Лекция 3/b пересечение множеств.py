set1 = set(list(map(int,input().split())))
set2 = set(list(map(int,input().split())))
ans = sorted(set1.intersection(set1,set2))
print(' '.join(map(str,ans)))