def binsearch(l, r, seq, num):
	while l < r:
		m = (l + r) // 2
		if seq[m] >= num:
			r = m	
		else:
			l = m + 1
	return seq[l] == num

N, K = map(int, input().split())
firstarr = list(map(int, input().split()))
secondarr = list(map(int, input().split()))

for i in range(len(secondarr)):
	check = binsearch(0, len(firstarr)-1, firstarr, secondarr[i])
	if check:
		print('YES')
	else:
		print('NO')