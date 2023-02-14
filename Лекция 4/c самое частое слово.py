def mostfreqword(text):
	textlist = text.split()
	textdict = {}
	maxfreq = 0
	for word in textlist:
		if word not in textdict:
			textdict[word] = 0
		textdict[word] += 1
		if textdict[word] > maxfreq:
			maxfreq = textdict[word]
	sorteddict = sorted(textdict.keys())
	for key in sorteddict:
		if textdict[key] == maxfreq:
			return key

text = []
with open('input.txt', 'r') as f:
	for x in f:
		text.append(x)

text = ' '.join(text)
ans = mostfreqword(text)
print(ans)