N = int(input())

for n in range(N,1000):
	str_n = list(str(n))
	if all([x==str_n[0] for x in str_n]):
		print(n)
		exit()