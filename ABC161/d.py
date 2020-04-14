import queue

K = int(input())

q = queue.Queue()
for i in range(9): q.put(i+1)

for _ in range(K):
	lunlun = q.get()
	
	if(lunlun%10)!=0: q.put(10*lunlun + lunlun%10 - 1)
	q.put(10*lunlun + lunlun%10)
	if (lunlun%10)!=9: q.put(10*lunlun + lunlun%10 + 1)

print(lunlun)