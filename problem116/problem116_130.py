S = input().strip()
T = input().strip()

num = 0
for s, t in zip(S, T):
    # print(s, t)
    if s != t:
        num += 1

print(num)