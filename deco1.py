import functools


class Foo():
    def __init__(self):
        self.state = False

    def _deco(cond):
        def _deco_(func):
            @functools.wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.state == cond:
                    return func(self, *args, **kwargs)
                else:
                    print('not ', end='')
                    return func(self, *args, **kwargs)

            return wrapper
        return _deco_

    @_deco(False)
    def bar(self):
        print('bar')

    def baz(self):
        self.state = not self.state


def main():
    foo = Foo()
    foo.bar()
    foo.baz()
    foo.bar()


if __name__ == '__main__':
    main()
