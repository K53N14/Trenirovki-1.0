def cosmobinsearch(l, r, n, a, b, w, h):
	while l < r:
		m = (l+r+1)//2
		if (w//(a + 2*m)) * (h//(b + 2*m)) >= n or (w//(b + 2*m)) * (h//(a + 2*m)) >= n:
			l = m
		else:
			r = m - 1
	return l


n, a, b, w, h = map(int, input().split())
a,b = max(a,b), min(a,b)
w,h = max(w,h), min(w,h)
ans = cosmobinsearch(0, n*w*h, n, a, b, w, h)
print(ans)




