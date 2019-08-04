n = int(input())
p = list(map(int, input().split()))

count = 0
for i,px in enumerate(p):
	if (i+1) != px:
		count += 1
	if count > 2:
		break

if count <= 2:
	print('YES')
else:
	print('NO')