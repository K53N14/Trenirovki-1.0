text = []
with open('input.txt', 'r') as f:
	for x in f:
		text.append(x)

buyers = {}

for entry in text:
	entry = list(entry.split())
	quantity = int(entry[2])
	name = entry[0]
	product = entry[1]
	if name not in buyers:
		buyers[name] ={}
	if product not in buyers[name]:
		buyers[name][product] = 0
	buyers[name][product] +=quantity

sortedbuyers = sorted(buyers.keys())

for name in sortedbuyers:
	print(name+':')
	sortedprods = sorted(buyers[name])
	for prod in sortedprods:
		print(prod, buyers[name][prod])