def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    counter = {}
    total = 0
    for num in A:
        total += num
        counter[num] = counter.get(num, 0) + 1

    Q = int(input())
    for i in range(Q):
        B,C = [int(i) for i in input().split()]
        if B in counter:
            B_cnt = counter[B]
            counter[C] = counter.get(C, 0) + B_cnt
            total += (C-B) * B_cnt
            counter[B] = 0
        print(total)

if __name__ == "__main__":
    solve()