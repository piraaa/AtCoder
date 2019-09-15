s = input()

odd = ['R','U','D']
even = ['L','U','D']

canTap = True

for i,n in enumerate(s):
	if (i+1)%2 != 0:
		if not (n in odd):
			canTap = False
			break
	
	if (i+1)%2 == 0:
		if not (n in even):
			canTap = False
			break

if canTap:
	print('Yes')
else:
	print('No')