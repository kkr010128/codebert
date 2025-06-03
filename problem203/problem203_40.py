def main():
    a, b = map(int, input().split(" "))
    for i in range(1,1010):
        ta = i*8//100
        tb = i*10//100
        if ta == a and tb == b:
            print(i)
            return
    print(-1)
    

if __name__ == "__main__":
    main()