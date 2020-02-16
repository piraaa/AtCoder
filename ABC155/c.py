import collections

N = int(input())

S = list()
for i in range(N): S.append(input())

c = collections.Counter(S)
max_value = c.most_common()[0][1]

ans = list()
for s in c.most_common():
	if s[1] == max_value:
		ans.append(s[0])
	else:
		break

ans.sort()
for a in ans:
	print(a)