N,M = map(int, input().split())
H = list(map(int, input().split()))
goodTowerFlag = [True] * N

for _ in range(M):
	a,b = map(int, input().split())
	if H[a-1] <= H[b-1]:
		goodTowerFlag[a-1] = False
	if H[b-1] <= H[a-1]:
		goodTowerFlag[b-1] = False

print(goodTowerFlag.count(True))