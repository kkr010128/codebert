# def main():
#     n, m = map(int, input().split())
#     ans = [0] * n
#     count = [0] * n
#     for i in range(m):
#         s, c = map(int, input().split())
#         if s == 1 and c == 0 and n != 1:
#             print(-1)
#             exit()
#         if count[s - 1] == 0 or ans[s - 1] == c:
#             ans[s - 1] = c
#             count[s - 1] += 1
#         else:
#             print(-1)
#             exit()
#     if ans[0] == 0 and n != 1:
#         ans[0] = 1
#     print(''.join(map(str, ans)))


# if __name__ == '__main__':
#     main()

def main():
    n, m = map(int, input().split())
    C = [-1] * n
    flag = 0
    for i in range(m):
        s, c = map(int, input().split())
        if C[s - 1] == -1 or C[s - 1] == c:
            C[s - 1] = c
        else:
            flag = 1

    if flag or (C[0] == 0 and n != 1):
        print(-1)
        return

    else:
        C = [0 if i == -1 else i for i in C]
        if C[0] == 0 and n != 1:
            C[0] = 1
    print(''.join(list(map(str, C))))


if __name__ == '__main__':
    main()
