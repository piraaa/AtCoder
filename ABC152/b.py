a,b = map(int, input().split())
ans = ''
if a<=b:
	for i in range(b): ans += str(a)
elif a>b:
	for i in range(a): ans += str(b)
print(ans)