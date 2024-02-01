from services.base_service import BaseService
from Common.Constant.Category import Category
from services.non_modify_services.stats_service import statsService
import time


# 没问题
class LoadsService(BaseService):
    To_load = []
    loadsame = 0  # 这个标志位用来判断加载的文件是否重复

    def read_line(self, file_path):
        with open(file_path, "r") as f:
            return [line.strip("\n") for line in f.readlines() if line.strip("\n")]

    def get_code(self):
        return "load"

    def get_category(self):
        return Category.modify

    def process(self, data):
        # load ⽂件路径
        data = data.split(" ", 1)  # 这里把 load ⽂件路径 分成两块
        if len(data) < 2:
            raise Exception("参数格式错误")
        self.To_load.append(data)
        statsService.loadtxt.append(data[1])
        statsService.loadtime.insert(len(statsService.loadtime), time.time())
        try:
            for i in range(0, len(self.file.filename)):
                if self.file.filename[i] == data[1]:
                    self.loadsame = 1
                    break
            if self.loadsame == 1:
                print("文件已经被加载到工作区了")
            else:
                self.file.filename.append(data[1])  # 加载文件名
                self.file.fileworkspace.append(1)
                self.file.filecontent.append(self.read_line(data[1]))
                self.file.content = self.read_line(data[1])
                self.file.file_workspace = len(self.file.filename) - 1

        except FileNotFoundError:
            print("文件不存在")
        except PermissionError:
            print("没有写入权限")

    def undo(self):
        self.file.content = []

    def redo(self):
        self.process("".join(["load ", self.To_load[len(self.To_load) - 1][1]]))
        self.To_load.pop()

    def init(self):
        Tempin = []
        Tempin = self.read_line(self, file_path="Temp.md")
        if Tempin == []:
            print("没有上一次的工作区记录")
        else:
            self.file.file_workspace = int(Tempin[0])
            for i in range(1, len(Tempin)):
                self.file.filename.append(Tempin[i])
            for i in range(0, len(self.file.filename)):
                self.file.fileworkspace.append(0)
            for i in range(0, len(self.file.filename)):
                self.file.filecontent.append(
                    self.read_line(self, file_path=self.file.filename[i])
                )
            self.file.content = self.file.filecontent[self.file.file_workspace]
