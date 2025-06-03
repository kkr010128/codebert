def insertionSort(R, n):
    for i in range(1, n):
        Now = R[i]
        j = i - 1
        while j >= 0 and R[j] > Now:
            R[j + 1] = R[j]
            j = j - 1
        R[j + 1] = Now
        trace(R, n)

def trace(R, n):
    for i in range(n):
        print R[i],
    print

n = input()
R = map(int, raw_input().split())

trace(R, n)
insertionSort(R, n)