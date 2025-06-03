#!/usr/bin/env python
#-*- coding:utf-8 -*-


def selectionSort(arr, N): 
    counter = 0 
    for i in range(N):
        minj = i 
        for j in range(i,N):
            if arr[minj] > arr[j]:
                minj = j 
        if minj != i: counter += 1
        arr[i], arr[minj] = arr[minj],arr[i]

    return counter,arr

def main():

    N = int(raw_input())
    A = map(int, raw_input().split())
    
    counter,sortedA = selectionSort(A, N)
    print ' '.join(map(str,sortedA))
    print counter

#def test():

if __name__ == '__main__':
    main()