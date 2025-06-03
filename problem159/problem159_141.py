x = int(input())

balance = 100
years = 0

while True:
    years += 1
    balance += balance // 100
    if balance >= x:
        print(years)
        exit(0)