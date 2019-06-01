n,m = map(int, input().split())
 
min = 1
max = n
 
for i in range(m):
	l,r = map(int, input().split())
	if l > max or r < min:
		max = 0
		min = 1 # ans表示時の+1を相殺
		break
	if min < l:
		min = l
	if max > r:
		max = r
 
print(max-min+1)