def copy_doc(func):
    def decorator(next_func):
        next_func.__doc__ = getattr(func, "__doc__", "")
        return next_func

    return decorator
