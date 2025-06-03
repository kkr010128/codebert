n = int(raw_input())
A = map(int, raw_input().split(" "))

def printElem(B):
    string = ""
    for elem in B:
        string += str(elem) + " "
    print(string[:len(string)-1])

printElem(A)

for i in range(1, n):
    key = A[i]
    j = i - 1

    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1

    A[j+1] = key

    printElem(A)