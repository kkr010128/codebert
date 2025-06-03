import sys
N=input()
i = 1
for i in range(1,N+1):
    if (i % 3) == 0 :
        sys.stdout.write(" ")
        sys.stdout.write("%d" % i)
    else:
        if (i % 10 ) == 3 :
            sys.stdout.write(' ')
            sys.stdout.write("%d" % i)
        else:
            if (i/10)%10 == 3:
                #print (i/10)%10,"a"
                sys.stdout.write(' ')
                sys.stdout.write("%d" % i)
            else:
                if (i/100)%10 == 3:
                    sys.stdout.write(' ')
                    sys.stdout.write("%d" % i)
                else:
                    if (i/100)%10 == 3:
                        sys.stdout.write(' ')
                        sys.stdout.write("%d" % i)
                    else:
                        if(i/1000)%10 == 3:
                            sys.stdout.write(' ')
                            sys.stdout.write("%d" % i)
print ""