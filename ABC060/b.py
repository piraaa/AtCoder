A,B,C = map(int, input().split())
for k in range(0,B+1,1):
	if k*A%B==C:
		print('YES')
		exit()
print('NO')