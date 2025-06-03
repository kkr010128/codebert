#https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_a
XY=input().split()
X=int(XY[0])
Y=int(XY[1])
award=0
if X==1 and Y==1:
    award+=400000
for num in [X,Y]:
    if num==3:
        award+=100000
    if num==2:
        award+=200000
    if num==1:
        award+=300000
print(award)