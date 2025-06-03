def main():
    input_line = raw_input()
    N = int(input_line)
    
    for i in range(N):
        input_line = raw_input()
        num_lis = []
        for num in input_line.split(' '):
            num_lis.append(int(num))
        num_lis.sort(reverse=True)
        if num_lis[0]**2 == num_lis[1]**2 + num_lis[2]**2:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()