def main4():
    N = int(input())
    S = input()

    R = set()
    G = set()
    B = set()

    for i in range(len(S)):
        if   S[i] == "R":
            R.add(i)
        elif S[i] == "G":
            G.add(i)
        elif S[i] == "B":
            B.add(i)

    ans = 0
    for r in R:
        for g in G:
            a, b = sorted([r, g])
            tmp = len(B)

            if ((b + a) % 2 == 0) and ((b + a) // 2) in B:
                tmp -= 1

            if (2*a - b) in B:
                tmp -= 1

            if (2*b - a) in B:
                tmp -= 1

            ans += tmp
                
    print(ans)

if __name__ == "__main__":
    main4()