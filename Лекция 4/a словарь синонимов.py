N = int(input())
syndict = {}
for i in range(N):
	words = input().split()
	syndict[words[0]] = words[1]
	syndict[words[1]] = words[0]

word = input()
print(syndict[word])