def main() :

    s = input()
    t = input()

    if (t in s) :
        print(0)
        return
    
    difference = 99999999
    for offset in range(0,len(s) - len(t)+1):
        s2 = s[offset:offset+len(t)]
        diff = 0
        for i in range(len(t)) :
            if (s2[i] != t[i]) :
                diff += 1
        
        if (difference > diff) :
            difference = diff
    
    print(difference)

main()