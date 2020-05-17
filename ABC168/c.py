import math

A,B,H,M = map(int, input().split())

ax = A * math.cos((180-(H*60+M))/720*2*math.pi)
ay = A * math.sin((180-(H*60+M))/720*2*math.pi)
bx = B * math.cos(((15-M)/60)*2*math.pi)
by = B * math.sin(((15-M)/60)*2*math.pi)

# print(ax,ay,bx,by)
print(math.sqrt((ax-bx)**2+(ay-by)**2))