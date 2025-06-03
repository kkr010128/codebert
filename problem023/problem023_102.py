

def solve():
    num_lines = int(raw_input())

    s = set()
    for i in xrange(num_lines):
        command, target = raw_input().split(" ")

        if command[0] == "i":# insert
            s.add(target)
            continue

        if target in s:
            print "yes"
        else:
            print "no"


if __name__ == "__main__":
    solve()