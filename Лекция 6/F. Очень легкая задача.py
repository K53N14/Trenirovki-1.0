def minprinttime(l, r, n, x, y):
	while l < r:
		m = (l + r)//2
		if m // x + m // y >= n:
			r = m
		else:
			l = m + 1
	return l + y

n, x, y = map(int, input().split())
x, y = max(x, y), min(x, y)
ans = minprinttime(0, x * n, n - 1, x, y)
print(ans)








