A, B, C, D = map(int, input().split())

T_HP = A
T_AT = B
A_HP = C
A_AT = D
T_count = 0
A_count = 0

while T_HP > 0:
    T_HP -= A_AT
    T_count += 1
while A_HP > 0:
    A_HP -= T_AT
    A_count += 1

if T_count > A_count:
    print('Yes')
elif T_count == A_count:
    print('Yes')
else:
    print('No')