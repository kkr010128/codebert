import copy
import math
import time
 
# a = get_int()
def get_int():
    return int(input())
# a = get_string()
def get_string():
    return input()
# a_list = get_int_list()
def get_int_list():
    return [int(x) for x in input().split()]
# a_list = get_string_list():
def get_string_list():
    return input().split()
# a, b = get_int_multi()
def get_int_multi():
    return map(int, input().split())
# a_list = get_string_char_list()
def get_string_char_list():
    return list(str(input()))
# print("{} {}".format(a, b))
# for num in range(0, a):
# a_list[idx]
# a_list = [0] * a
'''
while (idx < n) and ():
 
    idx += 1
'''
 
def main():
    start = time.time()
 
    n = get_int()
    s_list = get_string_char_list()
    s_list = [int(x) for x in s_list]
 
    #n = 30000
    #s_list = [1] * 30000
 
    #ans_set = set([])
 
    #for i in range(0,n):
    #    for ii in range(i+1, n):
    #        for iii in range(ii+1, n):
    #            ans_set.add(int(s_list[i]) * 100 + int(s_list[ii]) * 10 + int(s_list[iii]) * 1)
 
    #print(len(ans_set))
 
    ans = 0
 
    for i in range(0, 1000):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
 
        find_a = False
        find_b = False
        for ii in s_list:
 
            if (find_a == False) and (ii == a):
                find_a = True
            elif (find_a == True) and (find_b == False) and (ii == b):
                find_b = True
            elif (find_b == True) and (ii == c):
 
                ans += 1
                break
    print(ans)
 
    #print(time.time() - start)
 
if __name__ == '__main__':
    main()
 