N = int(input())

count = 0

for i in range(N):
	if (i+1)%3!=0 and (i+1)%5!=0:
		count += i+1

print(count)