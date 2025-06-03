N = int(input())
S = input() 
a=int(N/2)
if N%2==0 and S[:a]==S[a:]:
    print('Yes')
else:
    print('No')