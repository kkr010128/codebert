# ABC159
# String Palindrome
S = input()
n = len(S)
n
m = int(((n - 1)/2)-1)
l = int(((n + 3)/2)-1)

if S[::1] == S[::-1]:
        if S[:m+1:] == S[m::-1]:
            if S[l::] == S[:l-1:-1]:
                print('Yes')
                exit()
print('No')