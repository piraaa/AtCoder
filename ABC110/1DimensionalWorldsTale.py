n,m,x,y = map(int,input().split())
xn = list(map(int,input().split()))
ym = list(map(int,input().split()))

if not max(xn) < min(ym):
	print('War')
	exit()

z=max(xn)+1

if x<z<=y and max(xn)<z and z<=min(ym) :
	print('No War')
else:
	print('War')