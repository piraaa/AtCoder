N = int(input())
P = list(map(int, input().split()))

count = 0
min_value = 2e5+1

for p in P:
	if p <= min_value:
		min_value = p
		count += 1

print(count)