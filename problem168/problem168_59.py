summer_vacation, homework = map(int, input().split())
days = list(map(int, input().split()))

if summer_vacation < sum(days):                 # if elseを逆にするとerrorが出る
    print(-1)
else:
    print(summer_vacation-sum(days))