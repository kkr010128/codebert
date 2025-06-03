X=int(input())
i=0
while True:
    if 100*i<=X and X<=105*i:
        print(1)
        exit()
    elif 105*i<X and X<100*(i+1):
        print(0)
        exit()
    i+=1
