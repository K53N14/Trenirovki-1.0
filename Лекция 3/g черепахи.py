N = int(input())
ans = 0
truthful = set()
for i in range(N):
	a,b = list(map(int,input().split()))
	if a+b+1 == N and not (a<0 or b<0) and a not in truthful:
		truthful.add(a)
	
print(len(truthful))
