def e_yutori():
    # 参考: https://drken1215.hatenablog.com/entry/2020/04/05/163400
    N, K, C = [int(i) for i in input().split()]
    S = input()

    def sub_solver(string):
        """string が表す労働日時に対して、労働数が最大になるように働いたとき、
        i 日目には何回働いているかのリストを返す"""
        n = len(string)
        current, last = 0, -C - 1  # 最初に 'o' があっても動作するように設定
        ret = [0] * (n + 1)

        for i in range(n):
            if i - last > C and string[i] == 'o':
                current += 1
                last = i
            ret[i + 1] = current
        return ret

    left = sub_solver(S)
    right = sub_solver(S[::-1])
    ans = []
    for i in range(N):
        if S[i] == 'x':
            continue
        if left[i] + right[N - i - 1] < K:
            ans.append(i + 1)
    return '\n'.join(map(str, ans))

print(e_yutori())