n,k = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
while(True):
    if n <= k:
        ans += 1
        break
    
    n -= (k-1)
    ans += 1

print(ans)