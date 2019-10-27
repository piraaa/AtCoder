N = int(input())

divisors = []

for i in range(1, int(N**0.5)+1):
	if N % i == 0:
		y = i
		x = N//i

if y != 1:
	print((y-1)+(x-1))
else:
	print(x-1)