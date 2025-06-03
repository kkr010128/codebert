A, B, C = map(int, input().split())
K = int(input())

k = 0
while True:
    if A < B < C:
        print("Yes")
        break
    else:
        if k == K:
            print("No")
            break

        if B <= A:
            B *= 2
        elif C <= B:
            C *= 2
        k += 1