num = int(input())
val = 100000

for i in range(num):
    val = val * 1.05
    rem = val%1000
    if rem != 0:
        val = val - rem + 1000

print(int(val))
