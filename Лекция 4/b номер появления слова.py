def numofwords(text):
	textlist = text.split()
	textdict= {}
	ans = []
	for word in textlist:
		if word not in textdict:
			textdict[word] = 0
		ans.append(str(textdict[word]))
		textdict[word] += 1

	return ' '.join(ans)

text = []
with open('input.txt', 'r') as f:
	for x in f:
		text.append(x)

text = ' '.join(text)	
ans = numofwords(text)
print(ans)