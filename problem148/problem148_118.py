IN = [i for i in map(int,input().split())]
K = IN[3]
A = min(IN[0],K)
B = min(IN[1], K -A)
C = min(IN[2],K -A- B)
print(A*1+B*0+C*(-1))