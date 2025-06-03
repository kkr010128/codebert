if __name__ == '__main__':
    param_seconds = int(raw_input())

    seconds_per_hour = 60 * 60
    h = param_seconds / seconds_per_hour
    rest_seconds = param_seconds - h * seconds_per_hour

    m = rest_seconds / 60
    rest_seconds -= m * 60

    print "%s:%s:%s" % (h, m, rest_seconds)