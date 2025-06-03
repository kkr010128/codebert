def main():
    import re
    n = int(input())
    s = input()
    rindex = set()
    gindex = set()
    bindex = set()
    for i in range(n):
        if s[i] == "R":
            rindex.add(i)
        elif s[i] == "G":
            gindex.add(i)
        else:
            bindex.add(i)
    ans = len(rindex) * len(gindex) * len(bindex)

    for r in rindex:
        for g in gindex:
            if r > g:
                gap = r - g
                b1 = r + gap
                b2 = g - gap
                b3 = g + (gap/2)

            elif r < g:
                gap = g - r
                b1 = g + gap
                b2 = r - gap
                b3 = r + (gap/2)
            if b1 in bindex:
                ans -= 1
            if b2 in bindex:
                ans -= 1  
            if b3 in bindex:
                ans -= 1  
    print(ans)
if __name__ == "__main__":
    main()
