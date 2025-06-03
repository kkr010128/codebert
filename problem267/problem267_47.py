import itertools

def solve():     
    N = int(input())
    S = input()
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    p = itertools.product(l,repeat=3)
    count = 0
    for v in p:
        S_temp = S
        dig_0_index = S_temp.find(v[0])
        if dig_0_index != -1:
            S_temp = S_temp[dig_0_index+1::]
            dig_1_index = S_temp.find(v[1])
            if dig_1_index != -1:
                S_temp = S_temp[dig_1_index+1::]
                dig_2_index = S_temp.find(v[2])
                if dig_2_index != -1:
                    count += 1
    print(count)

if __name__ == "__main__":
    solve()