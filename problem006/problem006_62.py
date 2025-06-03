import math

in_week = int(input().rstrip())
tmp_debt = 100000

for i in range(in_week):
    tmp_debt = int(math.ceil( (tmp_debt*1.05)/1000.0 )) * 1000

print(str(tmp_debt))