n = int(input())

for i in range(1,11):
    if i==10:
        print("No")
        break
    if n%i == 0 and n/i < 10:
        print("Yes")
        break