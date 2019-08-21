# 相加相乗平均 (x+y)/2 >= sqrt(xy) より
# x+y=Aなので     A/2 >= sqrt(xy)
# 両辺二乗して (A/2)^2 >= xy
# よって最大値は (A/2)^2

a = int(input())
print((a//2)**2)