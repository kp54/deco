import functools


def _deco(tag):
    def _deco_(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return '<{0}>{1}</{0}>'.format(tag, func(*args, **kwargs))

        return wrapper
    return _deco_


# @_deco('html')
# @_deco('body')
# @_deco('p')
def foo():
    return 'Hello, world!'


def main():
    print(_deco('html')(_deco('body')(_deco('p')(foo)))())


main()
