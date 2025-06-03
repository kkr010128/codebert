import math

def main():
    X=int(input())

    for a in range(-120,120):
        flag=0
        for b in range(-120,120):
            if pow(a,5)-pow(b,5)==X:
                print("{} {}".format(a,b))
                flag=1
                break
        if flag==1:
            break

if __name__=="__main__":
    main()
