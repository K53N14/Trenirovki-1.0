def abinsearch(l, r, a,b,c):
	while l<r:
		m = (l+r) //2 
		if (a*2 + b*3 + c*4 + m*5)% (a+b+c+m) >= (a+b+c+m)//2 + (a+b+c+m)%2:
			prov = (a*2 + b*3 + c*4 + m*5) // (a+b+c+m) + 1
		else:
			prov = (a*2 + b*3 + c*4 + m*5) // (a+b+c+m)
		if prov >= 4:
			r = m 
		else:
			l = m + 1
	return l  

a = int(input())
b = int(input())
c = int(input())
ans = abinsearch(0, a+b+c, a,b,c)
print(ans)