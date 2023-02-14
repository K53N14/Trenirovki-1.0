def room_temp(troom, tcond, mode):
	if mode == 'freeze':
		if troom <= tcond:
			temp = troom
		else:
			temp = tcond

	if mode == 'heat':
		if troom >= tcond:
			temp = troom
		else:
			temp = tcond

	if mode == 'auto':
		temp = tcond

	if mode == 'fan':
		temp = troom
	return temp 
    
troom, tcond = map(int, input().split(' '))
mode = str(input())    

temp = room_temp(troom,tcond,mode)
print(temp)