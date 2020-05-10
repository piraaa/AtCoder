import math

X = int(input())
count = 0
deposit = 100

while deposit < X:
	deposit = math.floor(deposit * 1.01)
	count += 1

print(count)