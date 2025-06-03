S = input()
n = int(input())
for i in range(n):
    q = input().split()
    q[1] = int(q[1])
    q[2] = int(q[2])
    if q[0] == "print":
        print(S[q[1]:q[2] + 1])
    elif q[0] == "reverse":
        if q[1] == 0:
            S = S[:q[1]] + S[q[2]::-1] + S[q[2] + 1:]
        else:
            S = S[:q[1]] + S[q[2]:q[1] - 1:-1] + S[q[2] + 1:]
    elif q[0] == "replace":
        S = S[:q[1]] + q[3] + S[q[2] + 1:]