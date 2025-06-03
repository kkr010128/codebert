# coding: utf-8
# Here your code !

def shuffle_chars():

    chars = "chars"
    shuffle_num = "shuffle_num"

    #load data
    inputdata=[]
    i = -1
    while(True):
        try:
            line = input().rstrip()
            if line == "-" :
                break
            elif line.isalpha() :
                inputdata.append({chars: line, shuffle_num: []})
                tmp = input()
                i += 1
            else:
                inputdata[i][shuffle_num].append(int(line))
        except EOFError:
            break
        except :
            return inputError()

    #shuffle
    for item in inputdata:
        for num in item[shuffle_num] :
            item[chars] = item[chars][num:] + item[chars][:num]
        print(item[chars])

def inputError():
    print("input Error")
    return -1

if __name__ == "__main__" :
    shuffle_chars()