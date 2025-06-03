N = int(input())

# Nを 1以上 9以下の 2つの整数の積として表すことができるなら Yes を、できないなら No を出力せよ。

for i in range(1, 9+1):
    for j in range(1, 9+1):
        if i * j == N:
            print("Yes")
            exit()
else:
    print("No")