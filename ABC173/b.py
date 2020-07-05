N = int(input())
results = ['AC', 'WA', 'TLE', "RE"]
d = {'AC':0, 'WA':0, 'TLE':0, 'RE':0}

for _ in range(N):
	r = input()
	d[r] += 1

for i in range(4):
	print(results[i] + ' x ' + str(d[results[i]]))