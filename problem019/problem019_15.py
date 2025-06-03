# coding:utf-8
# Round-robin scheduling

def main():
    n, q = map(int, input().split())
    process = []
    finished = []
    counter = 0
    for _ in range(n):
        name, time = input().split()
        process.append((name, int(time)))

    while len(process)  > 0:
        name, time = process.pop(0)
        temp_q = q

        while True:
            
            if time <= 0:
                finished.append((name, counter))
                break

            # q????????§??????????¶????????????£???????????????
            # time?????´??°??????process???????°?????§???? 
            if temp_q <= 0:
                process.append((name, time))
                break
            
            time -= 1
            temp_q -= 1
            counter += 1
    
    for name, time in finished:
        print(name, time)

if __name__ == "__main__":
    main()