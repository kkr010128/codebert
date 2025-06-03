x = int(input())
ans = ''
if 400 <= x < 600:
    ans = '8'
elif x < 800:
    ans = '7'
elif x < 1000:
    ans = '6'
elif x < 1200:
    ans = '5'
elif x < 1400:
    ans = '4'
elif x < 1600:
    ans = '3'
elif x < 1800:
    ans = '2'
elif x < 2000:
    ans = '1'
print(ans)
