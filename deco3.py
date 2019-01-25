import functools


def _deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('--head--')
        tmp = func(*args, **kwargs)
        print('--tail--')
        return tmp

    return wrapper


@_deco
def hail(world='world'):
    print('Hello, {}!'.format(world))


hail()
