import numpy as np

N,M = map(int, input().split())

friendsMap  = np.array([[0 if i!=j else 1 for i in range(N)] for j in range(N)])

for i in range(M):
	a,b = map(int,input().split())
	if not friendsMap[a-1][b-1]:
		friendsMap[a-1][b-1] = 1
		friendsMap[b-1][a-1] = 1

print(max(np.sum(friendsMap, axis=1)))