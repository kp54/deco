import functools


class Foo():
    def __init__(self):
        self.cond = False

    def _deco(cond):
        def _deco_(func):
            @functools.wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.cond == cond:
                    return func(self, *args, **kwargs)
                else:
                    return 'unconditional'

            return wrapper
        return _deco_

    def _print(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            print(func(self, *args, **kwargs))

        return wrapper

    @_print
    @_deco(True)
    def bar(self):
        return 'bar'

    def baz(self):
        self.cond = not self.cond
        return self.cond


def main():
    foo = Foo()
    foo.bar()
    foo.baz()
    foo.bar()

main()
