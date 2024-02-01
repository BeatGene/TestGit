# 我们这里定义了一个唯一文件，它的Content是一个列表，方便我们文本编辑
from Common.Utils.Singleton import singleton_wrapper


@singleton_wrapper
class File(object):
    def __init__(self):
        self.file_workspace = -1  # 这个数用于表示哪个文件正在作为workspce
        self.filename = []  # 这个列表用于存放文件名
        self.fileworkspace = []  # 这个列表用于存放文件状态  修改有没有被保存
        self.filecontent = []  # 这个列表用于存放所有文件的内容 列表里面套列表
        self.content = []
        self.content_num = []  # 这个列表的作用是存放树形数据，与self.content一一对应

    def Caculate(
        self,
    ):  # 这个方法用来根据self.content计算self.content_num 每一次self.content改变，都要使用这个方法
        for i in range(len(self.content)):
            if self.content[i][0] == "#":
                data = self.content[i].split(" ", 1)
                self.content_num.append(len(data[0]))
            else:
                if self.content[i - 1][0] == "#":
                    data = self.content[i - 1].split(" ", 1)
                    self.content_num.append(len(data[0]) + 1)
                else:
                    self.content_num.append(self.content_num[i - 1])
