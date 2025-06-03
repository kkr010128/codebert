debt = 100000
n=int(raw_input())
for i in range(1,n+1):
    debt = debt*1.05
    if(debt % 1000) != 0:
        debt = (debt - (debt%1000)) + 1000
print int(debt)