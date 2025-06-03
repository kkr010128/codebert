X = int(input())
if X >= 2100:
    print(1)
    exit()

for a in range(21):
    for b in range(21-a):
        for c in range(21-a-b):
            for d in range(21-a-b-c):
                for e in range(21-a-b-c-d):
                    for f in range(21-a-b-c-d-e):
                        if 100*a +101*b +102*c +103*d +104*e + 105*f == X:
                            print(1)
                            exit()

print(0)