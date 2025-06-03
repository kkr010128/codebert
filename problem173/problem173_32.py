N = int(input())

def isnot_fizzbuzz(number: int) -> bool:
    if (number) % 3 != 0 and (number) % 5 != 0:
        return True
    return False

def main():
    sum = 0
    for number in range(1, N + 1):
        if isnot_fizzbuzz(number) == True:
            sum += number
    print(sum)

if __name__ == "__main__":
    main()