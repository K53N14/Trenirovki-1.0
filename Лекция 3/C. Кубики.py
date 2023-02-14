N, M = map(int, input().split())
anya = []
borya = []
for i in range(N):
	anya.append(int(input()))
for i in range(M):
	borya.append(int(input()))

both = sorted(set(anya).intersection(set(anya), set(borya)))
anya = sorted(set(anya).difference(both))
borya = sorted(set(borya).difference(both))
print(len(both))
if len(both) !=0:
	print(' '.join(map(str,both)))
else:
	print(' ')
print(len(anya))
if len(anya) !=0:
	print(' '.join(map(str,anya)))
else:
	print(' ')
print(len(borya))
if len(borya) !=0:
	print(' '.join(map(str,borya)))
else:
	print(' ')