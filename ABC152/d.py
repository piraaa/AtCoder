N = int(input())

ans = 0
c = [[0]*10 for i in range(10)]

for i in range(N):
	n = str(i+1)
	c[int(n[0])][int(n[-1])] += 1

for i in range(10):
	for j in range(10):
		ans += c[i][j]*c[j][i]

print(ans)