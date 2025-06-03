def is_bingo(ary):
    flag = False
    for i in range(3):
        if ary[i][0] == "hit" and ary[i][1] == 'hit' and ary[i][2] == 'hit':
            flag = True
            break
        if ary[0][i] == "hit" and ary[1][i] == 'hit' and ary[2][i] == 'hit':
            flag = True
            break
    if ary[0][0] == "hit" and ary[1][1] == 'hit' and ary[2][2] == 'hit':
        flag = True
    if ary[0][2] == "hit" and ary[1][1] == 'hit' and ary[2][0] == 'hit':
        flag = True
    return flag

answer_seets = [[0,0,0] for _ in range(3)]
for i in range(3):
    tmp_lis = list(input().split())
    for idx, tmp in enumerate(tmp_lis):
        answer_seets[i][idx] = tmp
N = int(input())
for _ in range(N):
    b = input()
    for i in range(3):
        for j in range(3):
            if answer_seets[i][j] == b:
                answer_seets[i][j] = "hit"
                break
        else:
            continue
        break

if is_bingo(answer_seets):
    print('Yes')
else:
    print('No')