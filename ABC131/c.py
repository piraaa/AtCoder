import math
import fractions

def lcm(a,b):
	return a*b//fractions.gcd(a,b)

A,B,C,D = map(int, input().split())

nc = math.floor(B/C)-math.ceil(A/C) + 1 # N(C):Cで割れる数の個数
nd = math.floor(B/D)-math.ceil(A/D) + 1 # N(D):Dで割れる数の個数
ncd = math.floor(B/lcm(C,D))-math.ceil(A/lcm(C,D)) + 1 # N(C∩D):CでもDでもで割れる数の個数

print((B-A+1)-nc-nd+ncd)