def main():
    N = int(input())

    user_remarks = {}

    for i in range(1, N+1):
        A = int(input())
        user_remarks[i] = []

        for _ in range(A):
            user_id, is_honest = [int(x) for x in input().split()]
            user_remarks[i].append((user_id, is_honest == 1))

    max_count = 0

    for i in range(2**N):
        honest = {}
        is_ok = True
        for x in range(N):
            # フラグが経っている時 = 正直もの
            if ((i >> x) & 1):
                honest[x+1] = True

                if is_ok:
                    # 正直者の証言チェック
                    for user_remark in user_remarks[x+1]:
                        target_user = user_remark[0]
                        target_is_honest = user_remark[1]

                        # ターゲットは正直者である場合
                        if target_is_honest:
                            # 正直者ではなかったら矛盾している
                            if not ((i >> (target_user-1)) & 1):
                                is_ok = False

                        # ターゲットが不親切な人である場合
                        if not target_is_honest:
                            # 正直者だったら矛盾している
                            if ((i >> (target_user-1)) & 1):
                                is_ok = False

        if is_ok:
            max_count = max(max_count, len(honest))

    print(max_count)


if __name__ == '__main__':
    main()
