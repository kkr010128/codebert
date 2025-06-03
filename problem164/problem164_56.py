
A,B,C,D = map(int, input().split())
n = 0

if C%B ==0:
    if A-(C//B-1)*D > 0:
        print('Yes')
    else:
        print('No')
elif C%B != 0:
    if A-(C//B)*D > 0:
        print('Yes')
    else:
        print('No')
