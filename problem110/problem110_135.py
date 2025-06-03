import itertools

H, W, K = list(map(int,input().split()))
board = []
for i in range(H):
    row = input()
    board.append(row)

result = []
for n in range(len(board)+1):
    for conb in itertools.combinations(board, n):
        result.append(list(conb))

rotate_result = []
for i in range(len(result)):
    rotate_result.append([list(x) for x in zip(*result[i])])

ans = 0
result2 = []
for i in range(len(rotate_result)):
    for j in range(len(rotate_result[i])+1):
        for conb in itertools.combinations(rotate_result[i], j):
            result2.append(list(conb))
            l = list(itertools.chain.from_iterable(list(conb)))
            if l != []:
                count = 0
                for k in range(len(l)):
                    if l[k] == "#":
                        count += 1
                    if k == len(l)-1 and count == K:
                        ans += 1

print(ans)
