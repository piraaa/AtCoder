# 回文にならない = 同じ文字は2個以上離れている
# → 最も登場する文字の個数と最も登場しない文字の個数の差が1以下なら良い

S = input()

count = [0]*3

for s in S:
	if s == 'a':
		count[0] += 1
	if s == 'b':
		count[1] += 1
	if s == 'c':
		count[2] += 1

if max(count)-min(count) <= 1:
	print('YES')
else:
	print('NO')