def q_d():
    n = int(input())
    a = list(map(int, input().split()))

    break_num = 0
    current_index = 1
    for i in range(n):
        if a[i] == current_index:
            current_index += 1
        else:
            break_num += 1

    if break_num == n:
        print(-1)
    else:
        print(break_num)


if __name__ == '__main__':
    q_d()
