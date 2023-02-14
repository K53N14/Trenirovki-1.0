def keybord(kdurability, kpress):
	kpressdict = {}
	for num in kpress:
		if num not in kpressdict:
			kpressdict[num] = 0
		kpressdict[num] += 1

	for i in range(len(kdurability)):
		if i+1 not in kpressdict:
			print('NO')
		elif kpressdict[i+1]<=kdurability[i]:
			print('NO')
		else:
			print('YES')

n = input()
kdur = list(map(int, input().split()))
k = input()
kpress = list(map(int, input().split()))
keybord(kdur, kpress)