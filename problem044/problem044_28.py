import sys

def main():
    for line in iter(sys.stdin.readline, ""):
        #print (line)
        a = line.rstrip("\n")
        tmp = a.split(" ")
        a = int(tmp[0])
        b = int(tmp[1])
        n = int(tmp[2])
        cnt = 0
        for i in range(1, n+1):
            if (n % i == 0) and (a <= i and i <= b):
                cnt = cnt + 1
                #print (i)
        print (cnt)    
if __name__ == "__main__":
    main()