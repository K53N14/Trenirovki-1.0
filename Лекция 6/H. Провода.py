def cordlen(l, r, k, n, cords):
	while l < r:
		m = (l + r + 1)//2
		nowcords = [x//m for x in cords]
		nowsum = sum(nowcords)
		if nowsum >= k:
			l = m
		else:
			r = m - 1
	return l

N, K = map(int, input().split())
cords = []
for _ in range(N):
	cord = int(input())
	cords.append(cord)

ans = cordlen(0, max(cords), K, N, cords)
print( ans)






