def resolve():
    N = int(input())
    s = set()
    for _ in range(N):
        a, b = input().split()
        if a == "insert":
            s.add(b)
        else:
            if b in s:
                print("yes")
            else:
                print("no")


resolve()

