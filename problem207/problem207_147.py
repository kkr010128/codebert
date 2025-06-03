import sys
card = [ list(map(int,input().split())) for a in range(3) ]
N = int(input())
point = [ int(input()) for a in range(N) ]

# cut holes
for I in point:
    for J in card:
        if I in J:
            J.index(I)
            J[J.index(I)] = "H"
# vertical check
for K in range(3):
    check = set([ x[K] for x in card ])
    if len(check) == 1 and list(check)[0] == "H":
        print('Yes')
        sys.exit()
# horizon check
for L in card:
    check = set(L)
    if len(check) == 1 and list(check)[0] == "H":
        print('Yes')
        sys.exit()
# diagonal check
LtoR = set([ card[M][M] for M in range(3)])
RtoL = set([ card[M][-M-1] for M in range(3)])
if len(LtoR) == 1 and list(LtoR)[0] == "H" or  len(RtoL) == 1 and list(RtoL)[0] == "H":    
    print('Yes')
    sys.exit()
print('No')