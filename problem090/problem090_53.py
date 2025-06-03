def resolve():
    data = [len(x) for x in input().split("S") if x]
    print(max(data) if data else 0)
resolve()