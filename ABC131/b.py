import numpy as np

N,L = map(int, input().split())

apples = list()
for i in range(N):
	apples.append(L+(i+1)-1)

index = np.argmin(np.abs(apples))
ans = -1 * apples[index]

for a in apples:
	ans += a
print(ans)