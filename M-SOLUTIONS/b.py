s = input()
k = len(s)

if 15-k+s.count('o') >= 8:
	print('YES')
else:
	print('NO')