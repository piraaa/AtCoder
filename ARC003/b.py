N = int(input())
s = list()
for _ in range(N):
	tmp = input()
	s.append(tmp[::-1])

s.sort()

for str in s:
	print(str[::-1])