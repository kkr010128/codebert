N, B, R = list(map(lambda x: int(x), input().split(" ")))

print((N // (B + R)) * B + min([N % (B + R), B]))