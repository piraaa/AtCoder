import math

def comb(n,k):
	return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

n,k = map(int, input().split())

red_num = n-k
blue_num = k

for i in range(1,k+1):
	if n-k+1 < i:
		ans = 0
	else:
		ans = comb(red_num+1, i) * comb(blue_num-1, i-1)
	print(ans%(10**9+7))