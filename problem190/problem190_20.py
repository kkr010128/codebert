# String Palindrome
def is_palindrome(s):
    res = s == s[::-1]
    return res

S = input()
N = len(S)
ans = ['No', 'Yes'][is_palindrome(S) & is_palindrome(S[:((N-1)//2)]) & is_palindrome(S[((N+1)//2):])]
print(ans)