import itertools

N,M,Q = map(int, input().split())
series = list()

for i in range(Q):
	series.append(list(map(int,input().split())))

A = [x for x in range(1,M+1)]

max_score = 0
for a in itertools.combinations_with_replacement(A,N):
	score = 0
	for s in series:
		if (a[s[1]-1] - a[s[0]-1]) == s[2]:
			score += s[3]

	if score > max_score: max_score = score

print(max_score)