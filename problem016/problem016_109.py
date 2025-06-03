def show_list(a):
    for x in a:
        print x,
    print

def stable_check(sorted_values,sorted_suits,default_values,default_suits,n):
    for i in xrange(1,10):
        check_ss = []
        check_ds = []
        if i in sorted_values:
            for x in xrange(n):
                if i == sorted_values[x]:
                    check_ss.append(sorted_suits[x])
                if i == default_values[x]:
                    check_ds.append(default_suits[x])
            for x in xrange(len(check_ss)):
                if check_ss[x]!=check_ds[x]:
                    return "Not stable"
    return "Stable"

def bubble_sort(values,suits,n):
    flag = True
    while flag:
        flag = False
        for j in reversed(xrange(1,n)):
            if values[j] < values[j-1]:
                tmp = values[j]
                values[j] = values[j-1]
                values[j-1] = tmp
                tmp = suits[j]
                suits[j] = suits[j-1]
                suits[j-1] = tmp
                flag = True
    show_list(marge_suits_values(values,suits,n))
def selection_sort(values,suits,n):
    for i in xrange(n):
        minj = i
        for j in xrange(i,n):
            if values[j]<values[minj]:
                minj = j
        if minj!=i:
            tmp = values[i]
            values[i]=values[minj]
            values[minj]=tmp
            tmp = suits[i]
            suits[i]=suits[minj]
            suits[minj]=tmp
    show_list(marge_suits_values(values,suits,n))
def marge_suits_values(values,suits,n):
    ans = []
    for x in xrange(n):
        ans.append(suits[x]+str(values[x]))
    return ans

def main():
    n = input()
    a = raw_input().split()
    suits1 = []
    values1 =[]
    for x in xrange(n):
        suits1.append(a[x][0])
        values1.append(int(a[x][1]))
    suits2 = list(suits1)
    values2 = list(values1)
    bubble_sort(values1,suits1,n)
    print stable_check(values1,suits1,values2,suits2,n)

    values1 = list(values2)
    suits1 = list(suits2)
    selection_sort(values2,suits2,n)
    print stable_check(values2,suits2,values1,suits1,n)

if __name__ == '__main__':
    main()