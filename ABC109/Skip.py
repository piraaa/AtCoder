import numpy as np
import fractions
from functools import reduce

N,X = map(int, input().split())
x = list(map(int,input().split()))

city = sorted(x)
city.append(X)
city.sort()
city = np.array(city)

if N==1:
    print(abs(X-x[0]))
    exit()

costs = city[1:]-city[:-1]

d = reduce(fractions.gcd, costs)

print(d)