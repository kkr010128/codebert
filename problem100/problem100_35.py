X = int(input())
X -= 400
for i in range(8):
    if 200*i + 199 >= X and X >= 200*i:
        print(8-i)
