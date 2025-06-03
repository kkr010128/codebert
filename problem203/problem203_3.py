A, B = [int(n) for n in input().split(" ")]


XstartA = A / 0.08
XendA = (A + 1) / 0.08

XstartB = B / 0.1
XendB = (B + 1) / 0.1

start = XstartA
if XstartA < XstartB:
    start = XstartB

end = XendA
if XendB < XendA:
    end = XendB

S = int(start)
E = int(end) + 1

ans = -1
for i in range(S, E + 1):
    if start <= i and i < end:
        ans = i
        break

print(ans)