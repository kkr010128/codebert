S = input()
Q = int(input())
Query = [input() for _ in range(Q)]
inv = False
add = ['','']
for query in Query:
    if query[0]=='1':
        inv = not inv
    else:
        add[(query[2] == '1') ^ inv] += query[-1]
ans = add[1][::-1] + S + add[0]
if inv:
    ans = ans[::-1]
print(ans)
