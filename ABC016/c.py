N,M = map(int, input().split())

friends = [list() for i in range(N)]

for _ in range(M):
	a,b = map(int, input().split())
	friends[a-1].append(b-1)
	friends[b-1].append(a-1)

ans = list()
for i in range(N):
	n = []
	for friend in friends[i]:
		for tmp in friends[friend]:
			if (not tmp in friends[i]) and (tmp != i):
				if not tmp in n:
					n.append(tmp)
	ans.append(len(n))

for a in ans:
	print(a)