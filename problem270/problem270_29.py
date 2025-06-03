from calendar import day_name
s = input()

for i in range(7):
    if s == day_name[i][:3].upper():

        ans = 6 - i
        if ans == 0: ans += 7

        print(ans)
        break
