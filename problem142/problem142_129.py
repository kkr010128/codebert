def main():
    n = int(input())
    if n % 10 == 3:
        print("bon")
        return
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        print("pon")
        return 
    else:
        print("hon")
        return 
main()