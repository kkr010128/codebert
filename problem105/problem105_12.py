N = int(input())
a_list = list(map(int, input().split()))
#print(a_list)
myans = 0
for a, b in enumerate(a_list):
    #print(a,b)
    if (a+1)%2 != 0 and b%2 != 0:
        myans += 1
print(myans)