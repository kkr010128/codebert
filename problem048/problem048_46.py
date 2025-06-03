a = []
for i in range(0,2):
    a.append(input())
d = list(map(int,a[1].split()))
print('{} {} {}'.format(min(d),max(d),sum(d)))