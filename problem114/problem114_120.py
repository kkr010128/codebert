import numpy as np
#基本入力
D = int(input())
c =list(map(int,input().split()))
s = []
for i in range(D):
        s.append(list(map(int,input().split())))
t = []
for i in range(D):
    t.append(int(input()))
        
#基本入力完了
#得点計算
c = np.array(c)
last_day = np.array([0]*26)
day_pulse = np.array([1]*26)
s = np.array(s)
t = np.array(t)
manzoku = 0
for day in range(1,D+1):
    contest_number = t[day-1] #開催するコンテスト種類
    manzoku += s[day-1,contest_number-1] #開催したコンテストによる満足度上昇
    last_day += day_pulse #経過日数の計算
    last_day[contest_number -1 ] = 0 #開催したコンテスト種類の経過日数を0に
    manzoku -= sum(c*last_day) #開催していないコンテストによる満足度の減少
    print(manzoku)
