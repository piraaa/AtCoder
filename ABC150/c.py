import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

p = 0
q = 0

for i in range(N-1):
	tmp = 0
	n = P.pop(0)
	for x in range(N):
		if not (x+1 in P) and x+1 < n : tmp += 1
	p += (n-tmp-1) * math.factorial(N-(i+1))
	
	tmp = 0
	n = Q.pop(0)
	for x in range(N):
		if not (x+1 in Q) and x+1 < n : tmp += 1
	q += (n-tmp-1) * math.factorial(N-(i+1))

print(abs(p-q))