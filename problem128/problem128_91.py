N, M = map(int, input().split())

x = list(map(int, input().split()))

#print(N)
#print(M)
#print(x)

def hantei(number_1, list_1):
    for a in range(101):
        a_plus = number_1 + a
        a_minus = number_1 - a

        if a_minus not in list_1:
            return a_minus
            break
        elif a_plus not in list_1:
            return a_plus
            break
    
print(hantei(N,x))



