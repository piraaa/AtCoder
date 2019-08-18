n = int(input())
v = list(map(int, input().split()))

for i in range(n-1):
	v.sort()
	x = v[0]
	y = v[1]
	v.remove(x)
	v.remove(y)
	v.append((x+y)/2)

print(v[0])