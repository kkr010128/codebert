n = int(input())
a = n // 1000
if n % 1000 != 0:
    b = a + 1
    print(f"{1000*b-n}")
else:
    print("0")