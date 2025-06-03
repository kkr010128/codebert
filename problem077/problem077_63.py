import sys

sys.setrecursionlimit(1000000)


def main():
    a, b, c, d = map(int, input().split())
    
    max_ab = max(a, b)
    min_ab = min(a,b)
    max_cd = max(c,d)
    min_cd = min(c,d)
    
    # ab ++
    if min_ab >= 0:
        # cd ++
        if min_cd >= 0:
            # ++
            print(max_ab * max_cd)
        # cd +-
        elif max_cd >= 0:
            # ++
            print(max_ab * max_cd)
        # cd --
        else:
            # +-
            print(min_ab * max_cd)
    # ab +-
    elif max_ab >= 0:
        # cd ++
        if min_cd >= 0:
            # ++
            print(max_ab * max_cd)
        # cd +-
        elif max_cd >= 0:
            # ++ or --
            print(max(max_ab * max_cd, min_ab * min_cd))
        # cd --
        else:
            # --
            print(min_ab * min_cd)
    # ab --
    else:
        # cd ++
        if min_cd >= 0:
            # -+
            print(max_ab * min_cd)
        # cd +-
        elif max_cd >= 0:
            # --
            print(min_ab * min_cd)
        # cd --
        else:
            # --
            print(min_ab * min_cd)


main()
