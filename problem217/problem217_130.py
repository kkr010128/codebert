def main():
    n = int(input())
    s = list(map(int,input().strip().split()))
    e = []
    for ss in s:
        if ss % 2 == 0:
            e.append(ss)
    
    for ee in e:
        if ee % 3 == 0 or ee % 5 == 0:
            continue
        else:
            print("DENIED")
            return
    
    print("APPROVED")
    return

main()
