def solve():
    from collections import deque
    K = int(input())
    q = deque([])
    cnt = 1
    while cnt <= K:
        if cnt < 10:
            q.append(cnt)
            cnt += 1
        else:
            base = q.popleft()
            last_digit = base % 10
            for diff in [-1, 0, 1]:
                if cnt > K:
                    continue
                new_last_digit = last_digit + diff
                if 0 <= new_last_digit <= 9:
                    new_lunlun = base*10 + new_last_digit
                    q.append(new_lunlun)
                    cnt += 1
    print(q[-1])

if __name__ == "__main__":
    solve()