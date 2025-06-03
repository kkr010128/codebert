#!/usr/bin/env python

def main():
    t = input()
    t_list = ['D']
    cnt = 0
    for s in t:
        if s == '?':
            cnt += 1
        else:
            if cnt > 0:
                t_list.append(cnt)
            cnt = 0
            t_list.append(s)
    if cnt > 0:
        t_list.append(cnt)
    t_list.append('P')

    for i in range(len(t_list)):
        if isinstance(t_list[i], int):
            k = t_list[i] // 2
            if t_list[i] % 2 == 0:
                if t_list[i-1] == 'P':
                    t_list[i] = 'D' + 'PD' * (k-1)
                    if t_list[i+1] == 'P':
                        t_list[i] += 'D'
                    else:
                        t_list[i] += 'P'
                else:
                    t_list[i] = 'PD' * k
            else:
                if t_list[i-1] == 'P':
                    t_list[i] = 'D' + 'PD' * k
                else:
                    t_list[i] = 'PD' * k
                    if t_list[i+1] == 'P':
                        t_list[i] += 'D'
                    else:
                        t_list[i] += 'P'

    print(''.join(t_list[1:-1]))

if __name__ == '__main__':
    main()
