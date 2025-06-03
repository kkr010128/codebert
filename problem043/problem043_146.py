import sys
def number():
    a = []
    b = []
    i = 0
    while True:
        x,y = map(int,input().split())
        if x == 0 and y == 0:
            break
        a.append(x)
        b.append(y)
        i += 1
    for j in range(len(a)):
        if a[j] < b[j]:
            print (a[j],b[j])
        else:
            print (b[j],a[j])

if __name__ == "__main__":
    number()