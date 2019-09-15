import numpy as np

N,M = map(int, input().split())
A = np.array(list(map(int, input().split())))

for _ in range(M):
	index = A.argmax()
	A[index] = A[index]//2
	
print(sum(A))