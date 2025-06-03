n = int(input())
i = 1
#end_check_num
while i <= n:
    #check_num
    x = i
    if x % 3 == 0:
        print(" %d" % i, end = "")
    else:
        #INCLUDE3
        while x != 0:
            if x % 10 == 3:
                print(" %d" % i, end = "")
                break
            x //= 10
    i += 1
print()