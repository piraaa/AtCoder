m = int(input())/1000

if m<0.1:
    VV = 0
elif 0.1<=m<=5:
    VV = m*10
elif 6<=m<=30:
    VV = m+50
elif 35<=m<=70:
    VV = (m-30)/5+80
elif 70<m:
    VV = 89

print('{:02}'.format(int(VV)))