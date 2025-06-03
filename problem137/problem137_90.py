def main():
    n = int(input())
    a_list = []
    b_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    a_sorted = list(sorted(a_list))
    b_sorted = list(sorted(b_list))
    if n%2:
        print(b_sorted[n//2]-a_sorted[n//2]+1)
    else:
        print((b_sorted[n//2-1]+b_sorted[n//2]-a_sorted[n//2-1]-a_sorted[n//2])+1)
        

if __name__ == "__main__":
    main()