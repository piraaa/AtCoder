N,T = map(int, input().split())

ans  = 1000+1 #問題文よりコストは最大で1000以下のため

for i in range(N):
	c, t = map(int, input().split())
	if  t <= T:
		if c <= ans:
			ans = c

if ans <= 1000:
	print(ans)
else:
	print('TLE')