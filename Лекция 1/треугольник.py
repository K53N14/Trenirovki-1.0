def triangle(a,b,c):
	if a+b > c and a+c>b and c+b > a:
		ans = 'YES'
	else:
		ans = 'NO'

	return ans

a = int(input())
b = int(input())
c = int(input())

tr = triangle(a,b,c)
print(tr)