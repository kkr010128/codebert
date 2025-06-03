n = int(input())
Mo = 100000
for i in range(n):
    Mo = Mo * 1.05
    if Mo%1000 != 0:
        Mo = (int(Mo/1000) + 1)*1000
print(int(Mo))