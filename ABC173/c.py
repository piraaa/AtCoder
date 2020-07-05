import copy
from itertools import combinations

def count_sharp(a):
	count = 0
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] == '#':
				count += 1
	return count

H,W,K = map(int, input().split())
h = [x for x in range(H)]
w = [x for x in range(W)]

c = list()
for i in range(H): c.append(list(input()))

h_sub = list()
for i in range(len(h) + 1):
	for con in combinations(h, i):
		h_sub.append(con)

w_sub = list()
for i in range(len(w) + 1):
	for con in combinations(w, i):
		w_sub.append(con)

count = 0
for h in h_sub:
	for w in w_sub:
		cc = copy.deepcopy(c)
		if len(h) != 0:
			for hh in h:
				width = len(cc[0])
				for j in range(width): cc[hh][j] = 'r'
		if len(w) != 0:
			for ww in w:
				height = len(cc)
				for i in range(height):
					cc[i][ww] = 'r'
		if count_sharp(cc) == K:
			count += 1

print(count)