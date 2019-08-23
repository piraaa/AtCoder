A,B = map(int, input().split())
dif = abs(A-B)

count = 0

while dif != 0:
	dif = min(abs(dif-10), abs(dif-5), abs(dif-1))
	count += 1

print(count)