S = input()
T = input()

min_dist = 10**10
for i in range(len(S) - len(T) + 1):
    for k in range(len(T)):
        dist = 0
        for s, t in zip(S[i:i + len(T)], T):
            if s != t:
                dist += 1
            if dist >= min_dist:
                break

        min_dist = min(dist, min_dist)
        if min_dist == 0:
            print(0)
            exit()

print(min_dist)
