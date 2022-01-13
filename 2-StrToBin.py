def strConvert(st, space=True):
    if space:
        return ' '.join([bin(ord(let))[2:] for let in st])
    return ''.join([bin(ord(let))[2:] for let in st])


print(strConvert('Hello world'))
