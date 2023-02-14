N = int(input())
whdict = {}
for i in range(N):
	w,h = list(map(int, input().split()))
	if w not in whdict:
		whdict[w] = h 
	elif h > whdict[w]:
		whdict[w] = h 
ans = 0
for w in whdict:
	ans += whdict[w]

print(ans)