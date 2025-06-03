n = int(input())

ab = [list(map(int, input().split())) for _ in range(n)]
ab_a = sorted(ab, key=lambda x:int(x[0]))
ab_b = sorted(ab, key=lambda x:int(x[1]))

if n%2 == 1:
    print(ab_b[n//2][1]-ab_a[n//2][0]+1)
else:
    print(int(((ab_b[n//2][1]+ab_b[n//2-1][1])/2.0-(ab_a[n//2][0]+ab_a[n//2-1][0])/2.0)*2+1))