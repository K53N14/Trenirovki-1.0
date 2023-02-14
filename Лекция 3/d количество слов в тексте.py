text = []
with open('input.txt', 'r') as f:
	for x in f:
		text.append(x)

text = ' '.join(text)

diction = set(text.split())
print(len(diction))
