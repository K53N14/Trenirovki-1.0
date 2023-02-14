def binsearch(l, r, seq, num):
	while l < r:
		m = (l + r) // 2
		if seq[m] >= num:
			r = m
		else:
			l = m + 1
	return l

N, K = map(int, input().split())
firstarr = list(map(int, input().split()))
secondarr = list(map(int, input().split()))

for i in range(len(secondarr)):
	pos = binsearch(0, len(firstarr)-1, firstarr, secondarr[i])
	ans = firstarr[pos]
	
	if pos > 0:
		ansdiff = max(firstarr[pos] - secondarr[i], secondarr[i] - firstarr[pos])
		provdiff = max(firstarr[pos - 1] - secondarr[i], secondarr[i] - firstarr[pos - 1])
		if provdiff <= ansdiff:
			ans = firstarr[pos - 1]

	print(ans)