def main():
    N = int(input())
    s={""}
    for _ in range(N):
        s.add(input())
    
    return len(s)-1

if __name__ == '__main__':
    print(main())