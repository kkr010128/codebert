def main():
    N = input() 
    a = [input() for y in range(N)] 
    a_max = -10**9
    a_min = a[0]
    for j in xrange(1,len(a)):
        if a[j] - a_min > a_max:
            a_max = a[j] - a_min
        if a[j] < a_min:
            a_min = a[j]
    print a_max
main()