S = input()
n = len(S)

s1 = S[:(n-1)//2]
s2 = S[(n+3)//2-1:]

if S[::-1]==S and s1[::-1]==s1 and s2[::-1]==s2:
    print("Yes")
else:
    print("No")