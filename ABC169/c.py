import math
from decimal import Decimal
A,B = input().split()
print(math.floor(Decimal(str(A))*Decimal(str(B))))