import math

N = int(input())
x = list()
for i in range(N):
	x.append(list(map(int, input().split())))

ans = 0
cities = [x for x in range(N)]
for i in range(N):
	tmp = 0
	cities.remove(i)
	for j in cities:
		tmp += math.sqrt((x[i][0]-x[j][0])**2+(x[i][1]-x[j][1])**2) * math.factorial(N-1) * 2
	ans += tmp
	
print(ans/math.factorial(N))
	