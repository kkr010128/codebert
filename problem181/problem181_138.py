import sys

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

K = int(input())

# indexは桁数
luns = [[]]
luns.append(list("123456789"))
for keta in range(2, 11):
    keta_lun = []
    for s in luns[-1]:
        lst = int(s[-1])
        if lst - 1 >= 0:
            keta_lun.append(s + str(lst - 1))
        keta_lun.append(s + str(lst))
        if lst + 1 < 10:
            keta_lun.append(s + str(lst + 1))
    luns.append(keta_lun)

index = 0
for keta_luns in luns:
    for lun in keta_luns:
        index += 1
        if index == K:
            print(lun)
            quit()