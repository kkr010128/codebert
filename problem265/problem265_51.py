import math

def main():

    n = int(input())
    tax = 1.08
    
    ans = math.ceil(n / tax)
    ans_check = ans * tax
    if math.floor(ans * tax) == n:
        print(ans)
    else:
        print(":(")
    
if __name__ == "__main__":
    main()