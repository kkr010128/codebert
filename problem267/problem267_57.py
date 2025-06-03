n = int(input())
s = input()
ans = 0
for pin in range(10**3):
    str_pin = str(pin)
    str_pin = str_pin.zfill(3)
    nex = 0
    for i in range(n):
        searching_for = str_pin[nex]
        now_s = s[i]
        if searching_for == now_s:
            nex += 1
            if nex == 3:
                ans += 1
                break
print(ans)

