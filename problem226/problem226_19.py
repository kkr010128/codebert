def atc_153b(a: str, b: str) -> str:
    HN = a.split(" ")
    H = int(HN[0])
    N = int(HN[1])

    A = b.split(" ")
    A_int = [int(ai) for ai in A]
    damage = sum(A_int)

    if (H - damage) <= 0:
        return "Yes"
    else:
        return "No"


a = input()
b = input()
print(atc_153b(a, b))