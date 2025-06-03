def solver(S,T):
    counter = 0
    for i in range(len(S)):
        Si = S[i]
        Ti = T[i]
        if Si != Ti:
            counter += 1
    return counter

S = input()
T = input()
print(solver(S,T))