tgtstr = list(raw_input())
n = int(raw_input())

for i in range(n):
    cmd_list = raw_input().split(" ")
    if cmd_list[0] == "replace":
        for idx in range(int(cmd_list[1]), int(cmd_list[2])+1):
            tgtstr[idx] = cmd_list[3][idx - int(cmd_list[1])]
    elif cmd_list[0] == "reverse":
        start = int(cmd_list[1])
        end = int(cmd_list[2])
        while True:
            
            tmp = str(tgtstr[start])
            tgtstr[start] = str(tgtstr[end])
            tgtstr[end] = tmp
            start += 1
            end -= 1
            if start >= end:
                break

    elif cmd_list[0] == "print":
        print "".join(tgtstr[int(cmd_list[1]):int(cmd_list[2])+1])