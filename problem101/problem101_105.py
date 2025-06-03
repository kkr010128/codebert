import itertools

a, b, c = map(int, input().split(" "))
k = int(input())
f = False
for conb in list(itertools.combinations_with_replacement([0, 1, 2], k)):
    a_i = conb.count(0)
    b_i = conb.count(1)
    c_i = conb.count(2)
    
    if (a * (2 ** a_i) < b * (2 **b_i)) and (b * (2 ** b_i) < c * (2 ** c_i)):
        f = True

if f:
    print("Yes")
else:
    print("No")