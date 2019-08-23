N = int(input())
C = [int(c) for c in input()]

max_num = 0
min_num = 0
max_correct = -1
min_correct = N+1

for i in range(1,5):
	count = 0
	for c in C:
		if i==c: count += 1
	if max_correct < count:
		max_correct = count
		max_num = i
	if min_correct > count:
		min_correct = count
		min_num = i

print(max_correct, min_correct)