X = list(map(int, input().split()))

for i in range(len(X)):
    if X[i] != i+1:
        print(i+1)


if __name__ == '__main__':
    print()