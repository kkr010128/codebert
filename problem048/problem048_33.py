input()
xs = list(map(int, input().split()))
print(' '.join(map(str,[f(xs) for f in [min,max,sum]])))