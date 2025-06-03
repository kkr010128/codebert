S = list(input())
Q = int(input())

c = 0
w = []

for i in range(Q) :
    a = input()
    if a[0] == "1" :
        c ^= 1
    else :
        if a[2] == "1" :
            if c == 0 :
                w.append(a[4])
            else :
                S.append(a[4])
        else :
            if c == 0 :
                S.append(a[4])
            else :
                w.append(a[4])
S = w[::-1] + S
print("".join(S) if c == 0 else "".join(S[::-1]))        