def biggestmult(seq):
	max1 = seq[0]
	max2 = seq[1]
	min1 = seq[0]
	min2 = seq[1]
	if max1<max2:
		temp = max1
		max1 = max2
		max2 = temp
	if min1>min2:
		temp = min1
		min1 = min2
		min2 = temp
	for i in range(2, len(seq)):	
		if seq[i] >= max1:
			max2 = max1
			max1 = seq[i]
		elif seq[i]> max2:
			max2 = seq[i]

		if seq[i]<=min1:
			min2 = min1
			min1 = seq[i]
		elif seq[i]< min2:
			min2 = seq[i]

	if max1*max2 > min1*min2:
		return(max2,max1)
	else:
		return(min1,min2)


seq = list(map(int, input().split()))
mult1,mult2 = biggestmult(seq)
print(mult1,mult2)