N, A, B = map(int, input().split())

if A == 0:
    print(0)
    exit()

quotient = N // (A + B) * A
remainder = N % (A + B)

quotient += min((remainder, A))

print(quotient)