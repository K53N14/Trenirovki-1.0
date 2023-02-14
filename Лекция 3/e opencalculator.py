buttons = set(map(int, input().split()))
nums = input()
numlist = []
for num in nums:
	numlist.append(int(num))

numset = set(numlist)
if numset.issubset(buttons):
	print(0)
elif len(numset.difference(buttons)) !=0:
	print(len(numset.difference(buttons)))
