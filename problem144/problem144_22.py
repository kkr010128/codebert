from math import cos, radians

def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) / 2 # 時針の角度
    m_angle = m * 6 # 分針の角度
    theta = abs(h_angle - m_angle)
        
    x_2 = a**2  + b**2 - 2*a*b*cos(radians(theta))
    print(x_2 ** 0.5)
    
main()