import heapq

N,M = map(int, input().split())
A = list(map(lambda x:int(x)*(-1), input().split()))
heapq.heapify(A)

for _ in range(M):
	min_value = heapq.heappop(A)
	heapq.heappush(A, (-min_value//2)*(-1))
	
print((-1)*sum(A))