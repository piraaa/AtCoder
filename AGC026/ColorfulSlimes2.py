N = int(input())
a = times = [int(i) for i in input().split()]

i = 0
count = 0
ans = 0

while(i<(N-1)):
    while(a[i] == a[i+1]):
        count += 1
        i += 1
        if i >= (N-1):
            break
    ans += (count+1)//2
    i += 1
    count = 0

print(ans)