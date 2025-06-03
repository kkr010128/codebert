from itertools import combinations

def python_list_add(in1, in2):
   return list(map(sum, zip(in1, in2)))

N, M, X = map(int, input().split())
T = []
C = []
min = 10000000

for n in range(N):
    C.append(list(map(int, input().split())))

for bi in range(2**N):
    rikai = [0]*(M+1)
    low = False
    for i in range(N):
        b = 2**i
        if bi & b != 0:
            for j in range(M+1):
                rikai[j] = rikai[j] + C[i][j]
                #if rikai[0] > min:
                    #break
    #print(rikai)
    if rikai[0] < min:
        for m in range(1, M+1):
            if rikai[m] < X:
                low = True
                #print('low rikai')
                break
        if low == False:
            min = rikai[0]
if min == 10000000:
    print('-1')
else:
    print(min)