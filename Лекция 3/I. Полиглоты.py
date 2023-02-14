N = int(input())
langlist = {}
quanlang = 0
for i in range(N):
	M = int(input())
	for j in range(M):
		lang = input()
		if lang not in langlist:
			langlist[lang] = 0
		langlist[lang] += 1
		if langlist[lang] == N:
			quanlang += 1

print(quanlang)
for lang in langlist:
	if langlist[lang] == N:
		print(lang)

print(len(langlist))

for lang in langlist:
	print(lang)