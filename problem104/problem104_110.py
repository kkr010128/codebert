def main():
    
    input_lines_lrd = input()
    arrLRD = input_lines_lrd.split(" ")
    l = int(arrLRD[0])
    r = int(arrLRD[1])
    d = int(arrLRD[2])
    
    cnt = 0
    for n in range(l, r+1):
        if n % d == 0:
            cnt = cnt + 1
    
    print(cnt)
    
if __name__ == "__main__":
    main()
