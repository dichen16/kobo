# -*- coding: utf-8 -*-


__all__ = (
    "decorator_with_args",
    "well_behaved",
)


def decorator_with_args(old_decorator):
    """Enable arguments for decorators.

    Example:
    >>> @decorator_with_args
        def new_decorator(func, arg1, arg2):
            ...

        # it's the same as: func = new_decorator(func)("foo", "bar")
        @new_decorator("foo", "bar")
        def func():
            ...
    """

    def new_decorator_args(*nd_args, **nd_kwargs):
        def _new_decorator(func):
            return old_decorator(func, *nd_args, **nd_kwargs)

        _new_decorator.__name__ = old_decorator.__name__
        _new_decorator.__doc__ = old_decorator.__doc__
        if hasattr(old_decorator, "__dict__"):
            _new_decorator.__dict__.update(old_decorator.__dict__)

        return _new_decorator
    return new_decorator_args


def well_behaved(decorator):
    """Turn a decorator into the well-behaved one."""

    def new_decorator(func):
        new_func = decorator(func)
        new_func.__name__ = func.__name__
        new_func.__doc__ = func.__doc__
        new_func.__dict__.update(func.__dict__)
        return new_func

    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator
