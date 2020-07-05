N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

sum = A[0]
index = 1

for i in range(1,N-1):
	sum += A[index]
	if i%2 == 0:
		index += 1

print(sum)