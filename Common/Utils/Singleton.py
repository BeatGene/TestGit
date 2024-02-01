#这是一个装饰器工厂函数 用于保证我们修改的那个文本始终只有一个
def singleton_wrapper(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton