X=int(input())
han=0
for a in range(1001):
    if a * 100 > X:
        break
    for b in range(1001-a):
        if a * 100 + b * 101 > X:
            break
        for c in range(1001-a-b):
            if a * 100 + b * 101 + c * 102 > X:
                break
            for d in range(1001-a-b-c):
                if a * 100 + b * 101 + c * 102 + 103 * d> X:
                    break
                for e in range(1001-a-b-c-d):
                    if a * 100 + b * 101 + c * 102 + 103 * d + 104 * e>X:
                       break
                    for f in range(1001-a-b-c-d-e):
                        if a * 100 + b * 101 + c * 102 + 103 * d + 104 * e + 105 * f>X:
                            break
                        if a*100+b*101+c*102+103*d+104*e+105*f==X:
                            print("1")
                            han=1
                            exit()

if han==0:
    print(0)