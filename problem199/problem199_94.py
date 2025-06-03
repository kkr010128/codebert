def resolve():
    S = input()
    for i in range(0, len(S), 2):
        if not S[i:i + 2] == "hi":
            print("No")
            return
    else:
        print("Yes")


resolve()
