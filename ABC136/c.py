import numpy as np

n = int(input())
h = np.array(list(map(int, input().split())))

for i in range(n-1,0,-1):
	if h[i] >= h[i-1]:
		pass
	elif h[i] == h[i-1]-1:
		h[i-1] -= 1
	else:
		print('No')
		exit()
print('Yes')