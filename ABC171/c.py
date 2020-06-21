N = int(input())
ans = ''

while N > 26:
	N, mod = divmod(N-1, 26)
	ans = chr(ord('a')+mod) + ans

ans = chr(ord('a')+(N-1)%26) + ans

print(ans)