import itertools

def is_triangle(list_L):
    
    if (list_L[0] + list_L[1] > list_L[2]) and (list_L[1] + list_L[2] > list_L[0]) and (list_L[2] + list_L[0] > list_L[1]) :
        return True
    else :
        return False

def is_uniqueL(list_L):

    return len(list_L) == len(set(list_L))

N = int(input())
L = map(int,input().split())

comb_L = list(itertools.combinations(L, 3))

sum = 0

for a_comb_L in comb_L :

    if is_uniqueL(a_comb_L) == True and is_triangle(a_comb_L) == True:
        sum += 1

print(sum)