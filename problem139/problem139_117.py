H1,M1,H2,M2,k = map(int,input().split())

h = ((H2-1)-H1)*60
m = (M2+60)-M1
print((h+m)-k)