S, T = input(), input()

print(sum(x != y for x, y in zip(S, T)))