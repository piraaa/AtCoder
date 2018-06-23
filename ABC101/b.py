n = input()
sn = 0

for x in n:
    sn += int(x)

if int(n)%sn == 0:
    print('Yes')
else:
    print('No')