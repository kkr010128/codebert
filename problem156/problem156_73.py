def main():
    x = int(input())
    a_lst = []
    b_lst = []
    for i in range(400):
        a_lst.append(-200 + i)
    for i in range(400):
        b_lst.append(-200 + i)

    flag = False
    for i in range(len(a_lst)):
        for j in range(len(b_lst)):

            a = a_lst[i]
            b = b_lst[j]
            if a ** 5 - b ** 5 == x:
                print(a, b)
                flag = True
                break

        if flag:
            break


if __name__ == '__main__':
    main()