# wrap = (lambda tag: (lambda func: (lambda *args, **kwargs: ('<{0}>{1}</{0}>'.format(tag, func(*args, **kwargs))))))

wrap = lambda tag: lambda func: lambda *args, **kwargs: '<{0}>{1}</{0}>'.format(tag, func(*args, **kwargs))


def hello(name='world'):
    return 'hello, {}!'.format(name)


print(wrap('p')(hello)(name='KP'))

print(wrap('body')(wrap('p')(hello))(name='miyacorata'))

print(wrap('html')(wrap('body')(wrap('p')(hello)))(name='Fukusan64'))
