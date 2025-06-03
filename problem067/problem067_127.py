taro_p = 0
hana_p = 0
for i in range(input()):
    taro,hana = raw_input().split(' ')
    if taro > hana:
        taro_p = taro_p + 3
        hana_p = hana_p + 0
    elif taro < hana:
        taro_p = taro_p + 0
        hana_p = hana_p + 3
    else:
        taro_p = taro_p + 1
        hana_p = hana_p + 1

print taro_p,hana_p