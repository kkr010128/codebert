N = int(input())

for i in range(1, 50000):
    pay = int(i*1.08)
    if pay == N:
        print(i)
        break
    elif pay > N:
        print(':(')
        break