def biggerthanneighbours(seq):
	quantity = 0
	for i in range(1,len(seq)-1):
		if seq[i]> seq[i+1] and seq[i]> seq[i-1]:
			quantity+=1
	return quantity

seq= list(map(int,input().split()))
ans = biggerthanneighbours(seq)
print(ans)