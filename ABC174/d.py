N = int(input())
c = list(input())

count_r = c.count('R')
count = 0

for i in range(N):
	if count_r == 0: break
	if c[i] == 'W':
		count += 1
		count_r -= 1
	if c[i] == 'R':
		count_r -= 1

print(count)