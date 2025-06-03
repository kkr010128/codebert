given = input()

data = given.strip().split()
X = int(data[0])
Y = int(data[1])

i = 0
ashi = 0
while (i <= X):
    ashi = 2 * (X - i) + 4 * i
    if ashi == Y:
        print("Yes")
        break
    i = i + 1

if i == X + 1 and ashi != Y:
    print("No")