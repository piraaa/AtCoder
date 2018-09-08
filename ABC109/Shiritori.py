n = int(input())
w = list()
for i in range(n):
    w.append(input())

for i in range(n-1):
    if w[i][-1] != w[i+1][0]:
        print('No')
        exit()
    if w[i] in w[i+1:]:
        print('No')
        exit()

print('Yes')