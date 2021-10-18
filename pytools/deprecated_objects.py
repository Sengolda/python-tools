import functools
from warnings import warn


def deprecated(instead_use=None):
    def actual_decorator(o):
        @functools.wraps(o)
        def decorated(*args, **kwargs):
            message = ""
            if instead_use is not None:
                message += "{0.__name__} is deprecated, use {1} instead."
            else:
                message += "{0.__name__} is deprecated."
            warn(message.format(o, instead_use))
            return o(*args, **kwargs)

        return decorated

    return actual_decorator
