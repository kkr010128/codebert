def main():
    s = input()

    if s[-1]=='s':
        print(s,'es',sep='')
    else:
        print(s,'s',sep='')

if __name__ == "__main__":
    main()