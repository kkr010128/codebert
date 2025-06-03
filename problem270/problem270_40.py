import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    days = ['','SAT','FRI','THU','WED','TUE','MON','SUN']
    print(days.index(s))
    
if __name__ == '__main__':
    main()