N = int(input())
setsize = N
myset = [[] for _ in range(setsize)]

def add(x):
	place = x % N
	if x not in myset[place]:
		myset[place].append(x)

for i in range(N):
	x,y = list(map(int, input().split()))
	add(x)

ans = 0
for i in range(len(myset)):
	ans += len(myset[i])

print(ans)