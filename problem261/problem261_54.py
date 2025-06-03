def actual(s):
    N = len(s)
    count_operation = 0

    for i in range(N):
        head = s[i]
        tail = s[N - 1 - i]

        if head != tail:
            count_operation += 1

    return int(count_operation / 2)

s = input()
print(actual(s))
