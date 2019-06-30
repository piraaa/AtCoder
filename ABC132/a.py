inputstr = input()
s = list()
for ch in inputstr:
	s.append(ch)

for char in s:
	if s.count(char) != 2:
		print('No')
		exit()
print('Yes')