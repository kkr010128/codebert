n, m, x = map(int, input().split())
ca = []
for _ in range(n):
    ca.append(list(map(int, input().split())))


cost_max = 12 * (10 ** 5)
book_list = []
flag = 0
for i in range(2**n):
    book_num = 0
    book_list = []
    if i == 0:
        continue
    for j in range(n):
        if (i >> j) & 1:
            book_list.append(ca[j])
            book_num += 1
    for j in range(m):
        skill_revel = 0
        for k in range(book_num):
            skill_revel += book_list[k][j+1]
        if skill_revel >= x:
            if j == (m-1) and k == (book_num-1):
                cost = 0
                for l in range(book_num):
                    cost += book_list[l][0]
                if cost <= cost_max:
                    flag = 1 
                    cost_max = cost
            continue
        else:
            break

if flag == 0:
    print(-1)
else:
    print(cost_max)