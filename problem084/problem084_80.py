import sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    import os, zlib, base64
    open('tourist.pyx', 'wb').write(zlib.decompress(base64.b85decode("c${TY%Wi`(5WFMt58Fc(Xq*VD9x7D&BPj>l7_bTkIj*Ai>${5yulNExGoBr<UD>{aRttH)I;%|$Qg=gd9dxR@Di;P73FNP9dUGDQ<!!6lSu|K~YBh-_ms0mLUn?gYZW#)-aa9<|QdNMzm)C?=0Ye!0PSL>Nlrr!HyueleslJL(9LLK>v^G%;rmuCIg#qB2DZxNO4vB|vjcygBlZci;a!M4%3#=<-KH%*=17Q{aUKnzd7$r^Mh?)~>JZY8tu?FNSSF3obEX4)B&4>QOg%{W&$?iM3r$#)#@1-i<G$3Tv!!YO=a7HK93>>2bH|?5DKSQZ$O1|v2Wz}2I=r-M5)Wxd_@vZhgv>n8k$Q*}~?$i?{b`*|*!&44o)o(qXPyC2tN78cW$sb`#As%5$;I{B+f6Pb!JtGS5K99vu#l*|yora61crqIw#8`%bf6>w5x%@H*ya+t$KlVq{`2")))
    os.system('cythonize -i -3 -b tourist.pyx')
import tourist