if __name__ == "__main__":
    x1, x2 , x3, x4, x5 = map(int, input().split())
    X = [x1, x2 , x3, x4, x5]
    for i in range(5):
        if X[i] == 0:
            print(i+1)