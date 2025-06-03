import sys, re

def echo(A):
    for i, a in enumerate(A):
        if i < len(A) - 1:
            sys.stdout.write('%d ' % a)
        else:
            sys.stdout.write('%d\n' % a)

def insertionSort(A, N):
    echo(A)
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        echo(A)


n = int(raw_input())
a_text = raw_input()
splits = re.split(' ', a_text)
a = []
for i, s in enumerate(splits): 
    if s:
        a.append(int(s))

insertionSort(a, n)