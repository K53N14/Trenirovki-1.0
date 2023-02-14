def metro(a,b,n,m):
	atimemax = (a+1)*n+a
	atimemin = (a+1)*n - a
	btimemax = (b+1)*m+b 
	btimemin = (b+1)*m-b
	maxtime = min(atimemax,btimemax)
	mintime = max(atimemin,btimemin)
	if maxtime<mintime:
		print(-1)
	else:
		print(mintime, maxtime)

a = int(input())
b = int(input())
n = int(input())
m = int(input())
metro(a,b,n,m)