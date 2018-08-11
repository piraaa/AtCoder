n = int(input())
flag = False

while n>=4:
    if n%4==0 or n%7==0:
        flag = True
        print('Yes')
        break

    n -= 7

if not flag:
    print('No')