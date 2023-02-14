def diffshirtpants(shirts, pants):
	shirt1 = pants1 = 0
	bestdif = max(shirts[0] - pants[0], pants[0] - shirts[0])
	ansshirt = anspant = 0
	while shirt1 < len(shirts):
		if pants1 < len(pants):
			dif = max(shirts[shirt1] - pants[pants1], pants[pants1] - shirts[shirt1])
			if dif == 0:
				return shirts[shirt1], pants[pants1]
			elif dif < bestdif:
				bestdif = dif
				ansshirt = shirt1
				anspant = pants1
			if shirts[shirt1] > pants[pants1]:
				pants1 += 1
			else:
				shirt1 += 1
		else:
			return shirts[ansshirt], pants[anspant]


	return shirts[ansshirt], pants[anspant]


N = int(input())
shirts = list(map(int, input().split()))
M = int(input())
pants = list(map(int, input().split()))

shirt, pants = diffshirtpants(shirts, pants)

print(shirt, pants)




