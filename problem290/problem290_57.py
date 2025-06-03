N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
F = sorted(list(map(int, input().split())), reverse=True)


# にぶたん := N人のメンバーそれぞれが完食にかかる時間のうち最大値をxに以下にできるか？
ok, ng = 10 ** 12 + 1, -1
while ok - ng > 1:
    x = (ok + ng) // 2

    need_training = 0
    for a, f in zip(A, F):
        need_training += max(0, a - x // f)

        if need_training > K:
            ng = x
            break
    else:
        ok = x

print(ok)
