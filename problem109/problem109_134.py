def main():
    from sys import stdin

    readline = stdin.readline

    N = int(readline().rstrip())
    
    c0 , c1 , c2 , c3 = 0 , 0 , 0 , 0

    for i in range(N):
        test = readline().rstrip()

        if test == "AC":
            c0 += 1
        elif test == "WA":
            c1 += 1
        elif test == "TLE":
            c2 += 1
        elif test == "RE":
            c3 += 1

    c0 = "AC x " + str(c0)
    c1 = "WA x " + str(c1)
    c2 = "TLE x " + str(c2)
    c3 = "RE x " + str(c3)


    print(c0 + "\n" + c1 + "\n" + c2 + "\n" + c3)

main()