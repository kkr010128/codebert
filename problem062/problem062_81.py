while True:
    x = int(input())
    if x == 0:
        break
    SCORE = len(str(x))
    ans = 0
    amari=x
    for i in range(SCORE+1):
        ans += amari//10**(SCORE-i)
        amari = amari%10**(SCORE-i)
    print(ans)
