def isPalindrome(st):
    l = len(st)
    c = l//2
    if l%2 == 1:
        return st[:c] == st[c+1:][::-1]
    else:
        return st[:c] == st[c:][::-1]

S = input()
N = len(S)

if isPalindrome(S) and isPalindrome(S[:(N-1)//2]) and isPalindrome(S[(N+3)//2 - 1:]):
    print('Yes')
else:
    print('No')


