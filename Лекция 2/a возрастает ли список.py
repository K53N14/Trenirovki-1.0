def ascending_list(seq):
	ans = 'YES'
	if not (len(seq) == 0 or len(seq) ==1):
		for i in range(1,len(seq)):
			if seq[i]<= seq[i-1]:
				ans =  'NO'
			elif ans != 'NO':
				ans = 'YES'
	return ans



seq= list(map(int, input().split()))
ans = ascending_list(seq)
print(ans)