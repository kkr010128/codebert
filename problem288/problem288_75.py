def main():
    import math
    n = int(input())
    n_sq = int(math.sqrt(n)) + 1
    tmp = 10 ** 13
    for i in range(n_sq, 1, -1):
        if n % i == 0:
            j = n // i
            k = (i-1) + (j-1)
            if tmp > k :
                tmp = k
    if tmp != 10 ** 13:
        ans = tmp
    else:
        ans = n-1
    print(ans)


    
if __name__ == "__main__":
    main()
