N = int(input())
X = [int(_) for _ in input().split()]
Y = [int(_) for _ in input().split()]


def calc_dist_mink(list_x, list_y, p):
    list_xy = [abs(list_x[i] - list_y[i]) for i in range(len(list_x))]
    list_xy_p = [i ** p for i in list_xy]
    ans = sum(list_xy_p) ** (1 / p)
    return(ans)

list_ans = []
ans_1 = calc_dist_mink(X, Y, 1)
list_ans.append(ans_1)

ans_2 = calc_dist_mink(X, Y, 2)
list_ans.append(ans_2)

ans_3 = calc_dist_mink(X, Y, 3)
list_ans.append(ans_3)

ans_4 = max([abs(X[i] - Y[i]) for i in range(N)])
list_ans.append(ans_4)

for ans in list_ans:
    print(f"{ans:.5f}")
    
