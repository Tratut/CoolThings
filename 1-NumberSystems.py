def conv(x=1, base=10):
    """ Easy translation to different number systems """
    res = ''
    alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while x > 0:
        res += alf[x % base]
        x //= base
    return res[::-1]
