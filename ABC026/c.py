N = int(input())

subordinate = [[] for i in range(N)]
paying = [0] * N

for i in range(1,N):
	subordinate[int(input())-1].append(i)

for i in range(N-1, -1, -1):
	if subordinate[i] == []:
		paying[i] = 1
	else:
		maxPay = 0
		minPay = 1e9
		for j in subordinate[i]:
			if maxPay < paying[j]: maxPay = paying[j]
			if minPay > paying[j]: minPay = paying[j]
		paying[i] = maxPay + minPay + 1

print(paying[0])