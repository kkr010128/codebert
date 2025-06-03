X = int(input())

num = X // 100 + 1
calc = X % 100

for a in range(num):
    for b in range(num - a):
        for c in range(num - a - b):
            for d in range(num - a - b - c):
                for e in range(num - a - b - c - d):
                    for f in range(num - a - b - c - d - e):
                        if calc == 0*a + 1*b + 2*c + 3*d + 4*e + 5*f:
                            print(1)
                            exit()


print(0)