S = str(input())
le = len(S)
s = []

for i in range(le):
    s.append(S[i])

r = s.count("R")

if r == 0:
    print(0)
elif r == 1:
    print(1)
elif r == 2:
    if s[1] == "S":
        print(1)
    else:
        print(2)
elif r == 3:
    print(3)
