# 这个类用来区分我们的服务是否改变了文本，方便我们接下来进行undo和redo操作
# 今天解决list_tree问题 还有redo1问题
class Category(object):
    modify = 1
    non_modify = 2
