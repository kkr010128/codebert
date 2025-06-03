N = int(input())
S = input()

if N<4:
    print(0)
else:
    a = [0] * N
    R, G, B = 0, 0, 0
    for i in range(N):
        if S[i] == "R":
            a[i] = 1
            R += 1
        if S[i] == "G":
            a[i] = 2
            G += 1
        if S[i] == "B":
            a[i] = 4
            B += 1

    rgb = R * G * B
    cnt = 0
    for i in range(N-2):
        for d in range(1, (N-i-1) // 2+1):
            if a[i] + a[i+d] + a[i+2*d] == 7:
                cnt += 1

    print(rgb -cnt)
