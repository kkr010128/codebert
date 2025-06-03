A, B = map(int, input().split())

a = [i for i in range(int((A-1)*100/8 ), int((A+1)*100/8 ))]
b = [i for i in range(int((B-1)*100/10), int((B+1)*100/10))]

a = [i for i in a if int(i*0.08) == A]
b = [i for i in b if int(i*0.10) == B]

ans = list(set(a) & set(b))
if ans and min(ans) > 0:
    print(min(ans))
else:
    print(-1)
