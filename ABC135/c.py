n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.append(0)

ans = 0
yoryoku = 0 #i-1番目の勇者がi番目の街で倒せる数

for i in range(0,n+1):
	if yoryoku == 0: #前の勇者の余力がないとき
		if a[i] <= b[i]: #今の勇者が今の街で全部倒せるとき
			ans += a[i] #街iで勇者iが倒す数
			yoryoku = b[i] - a[i] #余力
		else: #今の勇者が今の街で倒しきれないとき
			ans += b[i] #街iで勇者iが倒す数
			yoryoku = 0 #余力はない
	
	else: #前の勇者の余力があるとき
		if a[i] <= (yoryoku + b[i]): #勇者たちが今の街のモンスターを全部倒せるとき
			ans += a[i] #街iで勇者i-1と勇者iが倒す数
			if(yoryoku>=a[i]): #前の勇者だけで全部倒せる時の余力
				yoryoku = b[i]
			else:
				yoryoku =  b[i]-(a[i]-yoryoku)
		else: #今の勇者が今の街で倒しきれないとき
			ans += b[i] + yoryoku #街iで勇者iが倒す数
			yoryoku = 0 #余力はない

print(ans)