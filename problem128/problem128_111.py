X, N = map(int, input().split(' '))
if N == 0:
    print(X)
else:
    ls = list(map(int, input().split(' ')))
    diff = -1
    for i in range(101, -1, -1):
        if i not in ls:
            if diff == -1:
                diff = abs(i - X)
                result = i
            else:
                diff = min(diff, abs(i - X))
                if diff == abs(i - X):
                    result = i
    print(result)