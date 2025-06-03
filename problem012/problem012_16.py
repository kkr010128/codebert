def main():
    N = int(input())
    print(IsPrime(N))

def IsPrime(N):
    count = 0
    for i in range(N):
        inputNum = int(input())
        if(inputNum == 2):
            count += 1
            continue
        elif(inputNum % 2 == 0):
            continue

        flag = 0
        for j in range(3, int(pow(inputNum, 1/2))+1):
            if(inputNum % j == 0):
                flag = 1
                break
            else:
                continue
        if(flag == 0):
            count += 1
    
    return count

if __name__ == '__main__':
    main()