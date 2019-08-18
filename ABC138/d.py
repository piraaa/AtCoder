n,q = map(int, input().split())

parentNodes = [0] * n #i番目のノードの親番号

for i in range(n-1):
	a,b = map(int, input().split())
	parentNodes[b-1] = a-1

counter = [0] * n

for _ in range(q):
	p,x = map(int, input().split())
	counter[p-1] += x

for i in range(1,n):
	counter[i] += counter[parentNodes[i]]

print(*counter)