N = int(input())
S = input()

if N % 2 != 0:
    print('No')
else:
    left = S[:N//2]
    right = S[N//2:]
    if left == right:
        print('Yes')
    else:
        print('No')
