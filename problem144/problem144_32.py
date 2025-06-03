def resolve():
    A, B, H, M = list(map(int, input().split()))
    ath = ((H*60+M)/(12*60))*360
    bth = M/60*360
    diff = abs(ath - bth) if abs(ath - bth) < 180 else 360-abs(ath - bth)
    import math
    print(math.sqrt((A**2)+(B**2)-2*A*B*math.cos(2*math.pi*diff/360)))


if '__main__' == __name__:
    resolve()