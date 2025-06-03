s = input()

if s == "S" :
    print('天気が雨である日が連続していた最大の日数を入力せよ')
elif s == "RRR" :
    print(3)
elif s == "RRS" or s =="SRR" :
    print(2)
elif s == "SSS" :
    print(0)
else :
    print(1)