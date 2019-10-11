S = list(input())
K = int(input())

tmp = S[0]
count = 1
S_num = list()
for i in range(1,len(S)):
	if S[i] == tmp:
		count += 1
	else:
		S_num.append(count)
		tmp = S[i]
		count = 1
S_num.append(count)

if len(S_num) == 1:
	print(len(S)*K//2)
else:
	if S[0] != S[-1]:
		S_num = list(map(lambda x: x//2, S_num))
		print(sum(S_num)*K)
	else:
		a = S_num[0]
		b = S_num[-1]
		S_num = list(map(lambda x: x//2, S_num))
		print(sum(S_num)*K - (a//2 + b//2 - (a+b)//2)*(K-1))