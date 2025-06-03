def main():
    from collections import deque

    K = int(input())
    if K <= 9:
        print(K)
        return
    
    q = deque()
    for i in range(1, 10):
        q.append(i)
    
    count = 9
    while True:
        get_num = q.popleft()
        for i in range(-1, 2):
            add_num = get_num % 10 + i
            if 0 <= add_num and add_num <= 9:
                q.append(get_num * 10 + add_num)
                count += 1
                if count == K:
                    print(q.pop())
                    return


if __name__ == '__main__':
    main()