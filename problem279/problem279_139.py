N = int(input())
S = input()
if(len(S)%2==0):
    if(S[:len(S)//2]==S[len(S)//2:]):
        print('Yes')
    else:
        print('No')
else:
    print('No')