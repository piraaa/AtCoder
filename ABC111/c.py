import collections

n = int(input())
v = list(map(int, input().split()))

even = collections.Counter(v[0::2])
odd = collections.Counter(v[1::2])

if even.most_common()[0][0] != odd.most_common()[0][0]:
	print(n-(even.most_common()[0][1])-(odd.most_common()[0][1]))
else:
	if len(even) == len(odd) == 1:
		print(n//2)
	else:
		print(min(n-(even.most_common()[0][1])-(odd.most_common()[1][1]), n-(even.most_common()[1][1])-(odd.most_common()[0][1])))