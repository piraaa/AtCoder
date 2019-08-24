M,D = map(int, input().split())

ans = 0
for i in range(1,M+1):
	m = i
	for j in range(1,D+1):
		d10, d1 = map(int, list(str(j).zfill(2)))
		if d1>=2 and d10>=2 and d1*d10==m:
			ans += 1

print(ans)