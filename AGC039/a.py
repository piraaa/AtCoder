S = list(input())
K = int(input())

count=0

isOdd = False
if K%2 != 0: isOdd = True

if K==1:
	for i in range(len(S)-1):
		if S[i] == S[i+1]:
			S[i+1] = '?'
			count += 1

else:
	S2 = S+S

	for i in range(len(S2)-1):
		if S2[i] == S2[i+1]:
			S2[i+1] = '?'
			count += 1
	
	if isOdd:
		K -= 1
	
	count *= K//2

	if S2[0] == S2[-1]:
		count += (K/2)-1

	if isOdd:
		S.insert(0, S2[-1])

		for i in range(len(S)-1):
			if S[i] == S[i+1]:
				S[i+1] = '?'
				count += 1

print(int(count))