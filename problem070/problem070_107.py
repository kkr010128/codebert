
#!/usr/bin/python
# -*- coding: utf-8 -*-

# def
def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(list(map(int,input().split())))
    return np.array(x)

def str_mtx(N):
    x = []
    for _ in range(N):
        x.append(list(input()))
    return np.array(x)

def int_map():
    return map(int,input().split())

def int_list():
    return list(map(int,input().split()))

def print_space(l):
    return print(" ".join([str(x) for x in l]))

# import
import numpy as np
import collections as col
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

# main
N,M =int_map()
AB = int_mtx(M)

n, _ = connected_components(csr_matrix(([1]*M, (AB[:,0]-1, AB[:,1]-1)),(N,N)))

print(n-1)