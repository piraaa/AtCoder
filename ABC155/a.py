a,b,c = map(int, input().split())

if (a==b and a!=c) or (b==c and b!=a) or (a==c and a!= b):
	print('Yes')
else:
	print('No')