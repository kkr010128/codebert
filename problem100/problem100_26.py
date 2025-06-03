X=int(input())
if X<=599:
    k=8
elif 600<=X<=799:
    k=7
elif 800<=X<=999:
    k=6
elif 1000<=X<=1199:
    k=5
elif 1200<=X<=1399:
    k=4
elif 1400<=X<=1599:
    k=3
elif 1600<=X<=1799:
    k=2
else:
    k=1
print(k)