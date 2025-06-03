import copy

def print_list(A):
    print(*A, sep=" ")

def swap(a, b):
    return b, a

def val(str):
    return int(str[1])

def is_stable(_in, _out, n):
    for i in range(0, n):
        for j in range(i+1, n):
            for a in range(0, n):
                for b in range(a+1, n):
                    if val(_in[i]) == val(_in[j]) and _in[i] == _out[b] and _in[j] == _out[a]:
                        return False
    return True

def print_stable(_in, _out, n):
    if is_stable(_in, _out, n):
        print("Stable")
    else:
        print("Not stable")    

def find_minj(A, i, n):
    minj = i
    for j in range(i, n):
        if val(A[j]) < val(A[minj]):
            minj = j
    return minj        

def bubble_sort(A, n):
    A0 = copy.copy(A)
    flg = 1 #逆の隣接要素が存在する
    i = 0
    while flg:
        flg = 0
        for j in range(n-1, i, -1):
            if val(A[j-1]) > val(A[j]):
                A[j-1], A[j] = swap(A[j-1], A[j])
                flg = 1
        i += 1
    print_list(A)
    print_stable(A0, A, n)

def selection_sort(A, n):
    A0 = copy.copy(A)
    for i in range(0, n):
        minj = find_minj(A, i, n)
        if val(A[i]) > val(A[minj]):
            A[i], A[minj] = swap(A[i], A[minj])
    print_list(A)
    print_stable(A0, A, n)

n = int(input())
A = list(map(str,input().split()))
B = copy.copy(A)

bubble_sort(A, n)
selection_sort(B, n)
