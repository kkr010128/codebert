X, Y, A, B, C = map(int, input().split())

tmp = sorted(map(int, input().split()), key=lambda x: -x)[:X] \
      + sorted(map(int, input().split()), key=lambda x: -x)[:Y] \
      + sorted(map(int, input().split()), key=lambda x: -x)

print(sum(sorted(tmp, key=lambda x: -x)[:X + Y]))
