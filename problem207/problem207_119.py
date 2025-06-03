def bingo():
    for i in a:
        if i[0] in b and i[1] in b and i[2] in b:
            return True
    for i in range(3):
        if a[0][i] in b and a[1][i] in b and a[2][i] in b:
            return True
    tmp=[(a[i][i] in b) for i in range(3)]
    if tmp.count(True)==3:
        return True
    tmp=[a[0][2] in b,a[1][1] in b,a[2][0] in b]
    if tmp.count(True)==3:
        return True
 
a=[[int(i)for i in input().split()]for j in range(3)]
n=int(input())
b=[int(input())for i in range(n)]
bingo=bingo()
print("Yes" if bingo else "No")