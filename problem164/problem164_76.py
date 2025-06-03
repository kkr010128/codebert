A, B, C, D = map(int, input().split())

takahashi_turn = True
while A > 0 and C > 0:
    if takahashi_turn:
        C = C - B
    else:
        A = A - D
    takahashi_turn = not takahashi_turn

if A > 0:
    print('Yes')
else:
    print('No')