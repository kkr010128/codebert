# ALDS1 : Dictionary

def main():
    n = input()
    dic = {}
    for i in xrange(n):
        command, ope = raw_input().split()
        if command == "insert":
            dic[ope] = 1
        elif command =="find":
            if ope in dic:
                print "yes"
            else:
                print "no"

if __name__ == '__main__':
    main()