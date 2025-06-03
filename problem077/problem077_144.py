def main():
    data = list(map(int, input().split()))
    ans = [data[0]*data[2],data[0]*data[3],data[1]*data[2],data[1]*data[3],]
    print(max (ans))
if __name__ == "__main__":
    main()