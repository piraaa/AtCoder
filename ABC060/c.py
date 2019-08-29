import numpy as np

N,T = map(int, input().split())
t = np.array(list(map(int, input().split())))

t = np.append(t[1:], t[-1]+T) - t #隣との差分の行列
t = list(sorted(t))

borderIndex = t.index(T)

ans = int(sum(t[0:borderIndex]) + np.int64(len(t[borderIndex:])*T))
print(ans)