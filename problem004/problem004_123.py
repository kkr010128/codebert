for i in range(input()):
    q = map(int,raw_input().split())
    q.sort()
    a = "YES" if q[0]**2 + q[1]**2 == q[2]**2 else "NO"
    print a