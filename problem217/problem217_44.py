n = int(input())
a = list(map(int, input().split()))

for n in a:
    if n % 2 == 0:
        if not n % 3 == 0 and not n % 5 == 0:
            print("DENIED")
            break
else:
    print("APPROVED")