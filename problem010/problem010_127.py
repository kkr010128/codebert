num = int(raw_input())
line = raw_input()

A = line.strip().split(" ")
print " ".join(A)
#A = map(int, item_str)

for i in range(1, num):
    v = int(A[i])
    j = i - 1
    for j in range(j, -1, -1):
        if int(A[j]) > v:
            A[j+1] = A[j]
            j -= 1
        else:
            break
    A[j+1] = str(v)
    #A_str = map(str, A)
    print " ".join(A)