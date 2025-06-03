if __name__ == "__main__":
    S = input()
    count_right = 0
    count_left = 0
    prev = ""
    a = []

    current = 0
    for i, s in enumerate(S):
        if prev == ">" and s == "<":
            a.append((count_left, count_right))
            count_left = 0
            count_right = 0
        if s == ">":
            count_right += 1
            prev = ">"
            # a.append((count_left)
        else:
            count_left += 1
            prev = "<"
    a.append((count_left, count_right))
    s = 0
    for x in a:
        large = max(x[0], x[1])
        small = min(x[0], x[1])
        s += sum(range(large + 1)) + sum(range(small))
    print(s)
