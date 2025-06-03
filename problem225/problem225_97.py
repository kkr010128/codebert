h, a = map(int, input().split())
ans = h/float(a)
if ans == float(int(ans)):
    print(int(ans))
else:
    print(int(ans)+1)