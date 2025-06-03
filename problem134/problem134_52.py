n = int(input())
a_lst = list(map(int, input().split()))
a_lst.sort()

if a_lst[0] == 0:
    answer = 0
else:
    answer = 1
    for i in range(n):
        a = a_lst[i]
        answer *= a

        if answer > 10 ** 18:
            answer = -1
            break

print(answer)