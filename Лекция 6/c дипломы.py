def sizebinsearch(l, r, w, h, n):
	while l<r:
		m = (l+r)//2

		if (m//w) * (m//h) >= n:
			r = m
		else:
			l= m + 1
	return l 


w,h,n = map(int, input().split())
r = max(w,h)
ans = sizebinsearch(0, r*n, w, h, n)
print(ans)