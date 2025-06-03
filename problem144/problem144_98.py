import math

def main():
    A, B, H, M = map(int, input().split())
    h_angle = 30 * H + 0.5 * M
    if h_angle <= 90:
        h_angle = math.radians(90 - h_angle)
    else:
        h_angle = math.radians(360 - (h_angle - 90))

    m_angle = 6 * M
    if m_angle <= 90:
        m_angle = math.radians(90 - m_angle)
    else:
        m_angle = math.radians(360 - (m_angle - 90))

    h_x = A * math.cos(h_angle)
    h_y = A * math.sin(h_angle)
    m_x = B * math.cos(m_angle)
    m_y = B * math.sin(m_angle)
    print(math.sqrt(abs(h_x - m_x)**2 + abs(h_y - m_y)**2))

if __name__ == '__main__':
    main()
