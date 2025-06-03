A, B = map(int, input().split())
if A <= B*2:
    print(0)
elif A > B*2:
    print(A-B*2)