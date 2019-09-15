N,M = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)

it = 0

for _ in range(M):
	A[it] = A[it]//2
	if it < N-1:
		if A[it] < A[it+1] and A[0] < A[it+1]:
			it += 1	
		else:
			A.sort(reverse=True)
			it = 0
	elif it == N-1:
		A.sort(reverse=True)
		it = 0

print(sum(A))