# coding: utf-8
def main():
    n, m = map(int, input().split())
    A_array = list(map(int, input().split()))
    
    tmp_A_array = [x for x in A_array if x >= sum(A_array)/(4*m)]
    
    # print(sum(A_array)/(4*m), tmp_A_array, m, sep="\n")
    if len(tmp_A_array) >= m:
        print("Yes")
    else:
        print("No")
    
main()
