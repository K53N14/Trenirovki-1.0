def tel_numbers(addnum, numb):
	def num_to_list(num):
		numlist = []
		for i in range(len(num)):
			if num[i].isdigit():
				numlist.append(int(num[i]))
		return numlist
	def take_num(num):
		code = [4,9,5]
		if len(num) == 11 and num[1:4] == code:
			num = num[4:]
		elif len(num) == 8 or len(num) ==11:
			num = num[1:]
		else:
			num = num
		return num
	addnum = take_num(num_to_list(addnum))
	numb = take_num(num_to_list(numb))

	if addnum == numb:
		ans = 'YES'
	else:
		ans = 'NO'

	return ans

addnum = input()
fnum = input()
snum = input()
thnum = input()

ot1 = tel_numbers(addnum,fnum)
print(ot1)
ot2 = tel_numbers(addnum,snum)
print(ot2)
ot3 = tel_numbers(addnum,thnum)
print(ot3)