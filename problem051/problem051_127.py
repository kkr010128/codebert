while True:
    h, w = map(int, input().split())
    if not h and not w:
        break
    result = []
    w2 = w >> 1
    if w % 2:
        for i in range(h):
            if i % 2:
                result.append(".#" * w2 + ".")
            else:
                result.append("#." * w2 + "#")
    else:
        for i in range(h):
            if i % 2:
                result.append(".#" * w2)
            else:
                result.append("#." * w2)
    print("\n".join(result) + "\n")