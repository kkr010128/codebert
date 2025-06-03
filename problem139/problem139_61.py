H1, M1, H2, M2, K = map(int, input().split())
T1, T2 = (H1 * 60 + M1), (H2 * 60 + M2)
print("{}".format((T2 - K) - T1))