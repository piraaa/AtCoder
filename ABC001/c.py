dig,dis = map(int,input().split())

dig /= 10
dis = round(dis/60+1e-10, 1)

if 11.25<=dig<33.75:
    dir = 'NNE'
elif 33.75<=dig<56.25:
    dir = 'NE'
elif 56.25<=dig<78.75:
    dir = 'ENE'
elif 78.75<=dig<101.25:
    dir = 'E'
elif 101.25<=dig<123.75:
    dir = 'ESE'
elif 123.75<=dig<146.25:
    dir = 'SE'
elif 146.25<=dig<168.75:
    dir = 'SSE'
elif 168.75<=dig<191.25:
    dir = 'S'
elif 191.25<=dig<213.75:
    dir = 'SSW'
elif 213.75<=dig<236.25:
    dir = 'SW'
elif 236.25<=dig<258.75:
    dir = 'WSW'
elif 258.75<=dig<281.25:
    dir = 'W'
elif 281.25<=dig<303.75:
    dir = 'WNW'
elif 303.75<=dig<326.25:
    dir = 'NW'
elif 326.25<=dig<348.75:
    dir = 'NNW'
else:
    dir = 'N'

if 0.0<=dis<=0.2:
    dir = 'C'
    w = 0
elif 0.3<=dis<=1.5:
    w = 1
elif 1.6<=dis<=3.3:
    w = 2
elif 3.4<=dis<=5.4:
    w = 3
elif 5.5<=dis<=7.9:
    w = 4
elif 8.0<=dis<=10.7:
    w = 5
elif 10.8<=dis<=13.8:
    w = 6
elif 13.9<=dis<=17.1:
    w = 7
elif 17.2<=dis<=20.7:
    w = 8
elif 20.8<=dis<=24.4:
    w = 9
elif 24.5<=dis<=28.4:
    w = 10
elif 28.5<=dis<=32.6:
    w = 11
elif 32.7<=dis:
    w = 12

print(dir,w)