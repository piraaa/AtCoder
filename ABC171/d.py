import collections

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = list()
C = list()
for i in range(Q):
	b,c = map(int, input().split())
	B.append(b)
	C.append(c)

c = collections.Counter(A)
# print(c)

sum_a = sum(A)

for i in range(Q):
	b_num = c[B[i]]
	diff = (C[i]-B[i]) * b_num
	c[C[i]] = c[B[i]] + c[C[i]]
	c[B[i]] = 0
	sum_a = sum_a + diff
	print(sum_a)