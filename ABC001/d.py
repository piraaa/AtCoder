N = int(input())
times = [[int(i) for i in input().split('-')] for j in range(N)]

for i in range(N):
    times[i][0] = times[i][0]//5*5
    times[i][1] = times[i][1]//5*5 if times[i][1]%5==0 else times[i][1]//5*5+5

times = sorted(times, key=lambda x: x[0])

i = 0
ans = list()
while i < N:
    start = times[i][0]
    end = times[i][1]
    j = i+1
    if j==N:
        ans.append([start,end])
        break
    while end >= times[j][0]:
        if end < times[j][1]:
            end = times[j][1]
        j += 1
        if j>=N: break
    ans.append([start,end])
    i = j

for time in ans:
    print('{:04d}-{:04d}'.format(time[0],time[1]))