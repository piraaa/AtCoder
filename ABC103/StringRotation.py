import sys

s = input()
t = input()

for i in range(len(s)):
    ans = s[i:]+s[0:i]
    if ans == t:
        print('Yes')
        sys.exit()

print('No')