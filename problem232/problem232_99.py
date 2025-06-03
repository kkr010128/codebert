A, B = map(str, input().split())
A_ans=''
B_ans=''

if min(A,B) == A:
    for a in range(int(B)):
        A_ans += A
    print(A_ans)
else:
    for b in range(int(A)):
        B_ans += B
    print(B_ans)
