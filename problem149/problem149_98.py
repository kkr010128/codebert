# coding: utf-8
# Your code here!
import itertools
import numpy as np

def main():
    
    N, M, X = map(int, input().split())
    for i in range(N):
        row = np.array(list(map(int, input().split())))
        # print(row)
        if i == 0:
            c_array = row[0].reshape(1, 1)
            a_matrix = row[1:].reshape(1, len(row[1:]))
        else:
            c_array = np.append(c_array, row[0])
            a_matrix = np.vstack([a_matrix, row[1:].reshape(1, len(row[1:]))])
    # print(c_array)
    # print(a_matrix)
    min_cost = float("inf")
    for i in range(1, N+1):
        for v in itertools.combinations(np.arange(N), i):
            tmp = a_matrix[v, :].sum(axis=0)
            cost = c_array[list(v)].sum()
            # print(tmp)
            if tmp.min() >= X and cost <= min_cost:
                min_cost = cost
                
    if min_cost == float("inf"):
        print("-1")
    else:
        print(min_cost)
    
main()