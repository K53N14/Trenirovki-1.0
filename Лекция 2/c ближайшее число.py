def closestnum(seq, num):
	dif = []
	for s in seq:
		if s == num:
			return s 
		else:
			dif.append(num - s)
	if dif[0]<0:
		minnum = -dif[0]
	else:
		minnum = dif[0]
	minind = 0
	for i in range(1,len(dif)):
		if dif[i]<0:
			if -dif[i]< minnum:
				minind = i
				minnum = -dif[i]
		else:
			if dif[i]< minnum:
				minind = i
				minnum = dif[i]
	return seq[minind]
length = input()
seq= list(map(int, input().split()))
num = int(input())
ans = closestnum(seq,num)
print(ans)