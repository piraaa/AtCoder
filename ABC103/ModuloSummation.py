N = int(input())
a = [int(i) for i in input().split()]

product = 1
for x in a:
    product *= x

ans = 0
for x in a:
    ans += ((product-1) % x)
print(ans)