MOD = 10**9+7

N,K = map(int, input().split())
A = list(map(int, input().split()))

X = 0 #A内の転倒数
for i in range(N):
	for j in range(i+1, N):
		if A[i] > A[j]:
			X += 1

Y = 0 #Aと隣のAの間の転倒数
for i in range(N):
	for j in range(N):
		if A[i] > A[j]:
			Y += 1

ans = (X * K + Y * K*(K-1)//2) % MOD
print(ans)