def main():
    x = int(input())
    a = 1
    b = 1
    
    for i in range(-118, 120):
        a = i
        for j in range(-118, 120):
            b = j
            if x == a**5 - b**5:
                ans = str(a) + ' ' + str(b)
                print(ans)
                return


if __name__ == '__main__':
    main()