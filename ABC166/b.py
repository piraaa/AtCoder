N,K = map(int, input().split())

A = list()
for _ in range(K):
	d = int(input())
	A += list(map(int, input().split()))

count = 0
for i in range(N):
	if not (i+1) in A: count += 1

print(count)