def main():
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    ans = 7 - day.index(s)
    print(ans)

if __name__ == '__main__':
    main()