x = list(input().split())
for i in range(5):
#    logging.debug("i = {},x[i] = {}".format(i, x[i])) #
    if x[i] == "0":
        print(i + 1)
        exit()

#    logging.debug("n = {},f = {},f**b = {}".format(n, f, f**b))  #
#logging.debug("デバッグ終了")#