N,K,Q = map(int, input().split())
A = list()
for _ in range(Q):
	A.append(int(input())-1)

points = [0]*N

for a in A:
	points[a] += 1

for point in points:
	if (Q-point) < K:
		print('Yes')
	else:
		print('No')