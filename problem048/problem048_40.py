def main():

    n = int(input())
    numbers = list(map(int, input().split()))
    ans1 = min(numbers)
    ans2 = max(numbers)
    ans3 = sum(numbers)
    print(ans1, ans2, ans3)






if __name__=="__main__":
    main()