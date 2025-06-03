s = list(input())
k = int(input())

if len(set(s)) == 1:
    print((len(s)*k)//2)
    exit()

def n_change(sss):
    s = sss.copy()
    x = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            s[i] = "X"
            x += 1
    return x

print(n_change(s) + (k-1) * (n_change(2*s) - n_change(s)))