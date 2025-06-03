ARGS=input().split()
N=int(ARGS[0])
R=int(ARGS[1])

if N >= 10:
    NAIBU = R
else:
    NAIBU = R + (100 * (10 - N))

print(str(NAIBU))