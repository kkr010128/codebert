import sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    import os, zlib, base64
    open('solve.pyx', 'wb').write(zlib.decompress(base64.b85decode("c${5PL2kn!5WHLRAEt*Sc1xnT$EfZ{QXc?Aiev-A^w7S(i%nyvdjV!=XLlAI+=#&ld75G{_6BK2??S|=#!1Dp(1{?w<EOJH&jTL@HQY%)aC=jklvR4;?)gb_s~ORZjk+vkuQcd-eLbh>;LBp^Q+bAC!>}aqjLG~crz;}Y^;(EQ@m_@lgV(U`W`;{yfWm0_EAQ}z^94c0uVBHK)Qq=(wdqwaiA+n#riW!1890MrFbt7Fmc{I(I_&yge_+@XXFrmPb^(T}@+K-OoQG<gI?wg5kYx8Fx996n97i-67Aq_^Fd5`{Y9X@l*7Q3aqT3`=MAG4pQ0gciq0}v|&@A`T&U#x^bc@>E@Z#6j>-vxWYSJk30!ifgSr*IRrv-diT7V=sza4$2?E")))
    os.system('cythonize -i -3 -b -j 36 solve.pyx')
import solve