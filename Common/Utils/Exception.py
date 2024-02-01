#一种用于处理异常的装饰器模式

import functools

def exception_wrapper():
    def helper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                print(str(err))
        return wrapper

    return helper