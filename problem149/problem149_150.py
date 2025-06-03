import itertools


def main():
    n, m, x = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    flag1 = True
    max_lst = []
    for i in range(m):
        understanding = 0
        for j in range(n):
            understanding += lst[j][i+1]
        max_lst.append(understanding)

    for i in range(len(max_lst)):
        maximum = max_lst[i]
        if maximum < x:
            cost = -1
            flag1 = False
            break

    if flag1:
        number = 1
        cost_lst = []
        while number <= n:   ##一冊laからどんどん増やす
            n_lst = []
            for i in range(n):
                n_lst.append(i)
            choice = list(itertools.combinations(n_lst, number))
            combination_number = len(choice)
            choice_number = len(choice[0])

            for i in range(combination_number):

                cost1 = 0
                understanding_lst = [0] * m
                for j in range(choice_number):  ##一組終了
                    choiced_number = choice[i][j]
                    cost1 += lst[choiced_number][0]

                    for k in range(1, m + 1):
                        unstg = lst[choiced_number][k]
                        understanding_lst[k - 1] += unstg

                over_x = 0
                for l in range(m):
                    understanding = understanding_lst[l]
                    if understanding >= x:
                        over_x += 1

                if over_x == m:
                    cost_lst.append(cost1)

            number += 1

        cost = min(cost_lst)

    print(cost)


if __name__ == '__main__':
    main()