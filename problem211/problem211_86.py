N, R = map(int, input().split())
print("{}".format(R if N >= 10 else R + 100 * (10 - N)))