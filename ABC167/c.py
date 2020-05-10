import itertools

N,M,X = map(int, input().split())
books = list()
for _ in range(N): books.append(list(map(int, input().split())))

MAX_COST = 1e5*12+1
min_cost = MAX_COST
selector = [i for i in range(N)]
for n in range(1, len(selector)+1):
	for conb in itertools.combinations(selector,n):
		cost = 0
		rikai = [0 for _ in range(M)]
		for sel in conb:
			cost += books[sel][0]
			for i in range(M): rikai[i] += books[sel][i+1]
		if all(a >= X for a in rikai):
			if cost < min_cost: min_cost = cost

if min_cost != MAX_COST:
	print(min_cost)
else:
	print(-1)