def main(lst):
    m_1, d_1, m_2, d_2 = lst[0], lst[1], lst[2], lst[3]

    before = False
    after = None

    lst_1 = [1, 3, 5, 7, 8, 10, 12]
    lst_2 = [2]
    lst_3 = [4, 6, 9, 11]

    if m_1 in lst_1:
        if d_1 == 31:
            before = True
            if m_2 == m_1 + 1 or m_2 == 1:
                if d_2 == 1:
                    after = True
        else:
            before = False
    elif m_1 in lst_2:
        if d_1 == 28:
            before = True
            if m_2 == 3:
                if d_2 == 1:
                    after = True
        else:
            before = False
    if m_1 in lst_3:
        if d_1 == 30:
            before = True
            if m_2 == m_1 + 1:
                if d_2 == 1:
                    after = True
        else:
            before = False

    if before == True and after == True:
        return 1
    else:
        return 0


if __name__ == '__main__':
    before = list(map(int, input().rstrip().split()))
    after = list(map(int, input().rstrip().split()))

    print(main(before + after))
