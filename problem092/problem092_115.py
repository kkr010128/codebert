def main():
    x,k,d = map(int,input().split(" "))

    if abs(x) % d == 0:
        exceed_num = (abs(x) // d)
    else:
        exceed_num = (abs(x) // d) + 1


    if k <= exceed_num :
        print(abs( abs(x) - (d*k) ))
    else:
        if (k - exceed_num) % 2 == 0:
            print(abs( abs(x) - (d*exceed_num) ))
        else:
            print(abs( abs(x) - (d*(exceed_num-1) )))



if __name__ == '__main__':
    main()