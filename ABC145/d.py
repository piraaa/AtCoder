import math

X,Y = map(int, input().split())

movableFlag = False

for x in range(X):
	y = X-x*2
	if x*2+y*1==X and x*1+y*2==Y:
		movableFlag = True
		break
	
if movableFlag:
	if x==0 or y==0:
		print(1)
	else:
		print(math.factorial(X-1) // (math.factorial(x) // math.factorial((X-1)-x)))
else:
	print(0)