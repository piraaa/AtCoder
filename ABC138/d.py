n,q = map(int, input().split())

tree = [[[] for i in range(2)] for j in range(n)]

for i in range(n-1):
	a,b = map(int, input().split())
	tree[a-1][1].append(b-1)
	tree[b-1][0].append(a-1)

counter = [0] * n

for i in range(q):
	p,x = map(int, input().split())
	counter[p-1] += x
	if tree[p-1][1] != []:
		queue = tree[p-1][1].copy()
		while queue != []:
			node = queue[0]
			counter[node] += x
			queue.extend(tree[node][1])
			queue.remove(node)

print(*counter)