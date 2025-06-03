A = list(map(int, input().split()))

#print(A)

def hantei(list):
    for a in range(len(list)):
        if list[a] == 0:
            return a+1

print(hantei(A))