W = raw_input().lower()
s = []
ans = 0
while True:
    T = map(str, raw_input().split())
    if(T[0] == "END_OF_TEXT"):
        break
    else:
        for i in range(len(T)):
            if(W == T[i].lower()):
                ans += 1
print(ans)