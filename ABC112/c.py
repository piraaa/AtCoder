X_MAX = 100+1
Y_MAX = 100+1

N = int(input())

X = []
Y = []
H = []

for i in range(N):
	x,y,h = map(int, input().split())
	if h!=0:
		X.append(x)
		Y.append(y)
		H.append(h)

if len(X) == 1:
	print(X[0], Y[0], H[0])
	exit()

for cx in range(X_MAX):
	for cy in range(Y_MAX):
		flag = False
		tmp_H = H[0] + abs(X[0]-cx) + abs(Y[0]-cy)
		for i in range(1,len(X)):
			if H[i] == max(tmp_H - abs(X[i]-cx) - abs(Y[i]-cy), 0):
				flag = True
			else:
				flag = False
				break
		if flag:
			print(cx, cy, tmp_H)
			exit()