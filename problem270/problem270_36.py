
def main():
    s = input()
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    ind = week.index(s)
    print(7 - (ind % 7))


if __name__ == "__main__":
    main()
