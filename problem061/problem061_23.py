#-*-coding:utf-8-*-

def main():
    string = input()
    answer=""
    for s in string:
        if s.islower()==True:
            answer+=s.upper()
        elif s.isupper():
            answer+=s.lower()
        else:
            answer+=s
    print(answer)

if __name__=="__main__":
    main()
