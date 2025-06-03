n, k = map(int, input().split())
a = list(map(int, input().split()))

mrk = [0] * n
plc = a[0] - 1
rp = 0 #ループに入った場所
rpc = -1#ループに入ってから
prc = 0#ループに入る前
for i in range(1, k + 1):
#    logging.debug(i)
    if rpc >= 0:
        rpc += 1
        if plc == rp:
#            logging.debug("prc{},rpc{}".format(prc,rpc))
            k = (k - prc) % rpc
#            logging.debug("k{},plc{}".format(k,plc))
            for i in range(k):
                plc = a[plc] - 1
#                logging.debug(plc)
            print(plc + 1)
            exit()
    if rpc == -1:
        prc += 1
    if mrk[plc] == 1 and rpc == -1:
        rp = plc
        rpc = 0
    mrk[plc] += 1
    if i < k:
        plc = a[plc] - 1
#    logging.debug("{},next{},{},roop{}".format(mrk,plc,prc,rpc))

print(plc + 1)