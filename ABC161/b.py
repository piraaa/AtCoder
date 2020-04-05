N,M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
votes = sum(A)

for a in A:
	if a/votes >= 1/(4*M):
		count += 1

if count >= M:
	print('Yes')
else:
	print('No')