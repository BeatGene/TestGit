from services.base_service import BaseService
from Common.Constant.Category import Category
import time


# 有问题 list index out of range
class statsService(BaseService):
    loadtxt = []  # 这个列表用来储存编辑过的所有文件
    loadtime = []  # 这个列表用来储存每个文件打开的时间
    Time = []  # 以秒为单位

    def get_code(self):
        return "stats"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        data = data.split(" ", 1)
        for i in range(0, len(self.loadtime) - 1):
            if len(self.loadtime) - 1 == 0:
                break
            self.Time.append(int(self.loadtime[i + 1]) - int(self.loadtime[i]))
        self.Time.append(time.time() - self.loadtime[len(self.loadtime) - 1])
        if len(data) < 2 or data[1] == "all":
            for i in range(0, len(self.loadtxt)):
                print(
                    str(self.loadtxt[i])
                    + " "
                    + str(self.Time[i] // 360)
                    + "时"
                    + str((self.Time[i] // 60 - (self.Time[i] // 360) * 60))
                    + "分"
                )
        else:
            print(
                str(self.loadtxt[len(self.loadtxt) - 1])
                + " "
                + str(self.Time[len(self.loadtxt) - 1] // 360)
                + "时"
                + str(
                    self.Time[len(self.loadtxt) - 1] // 60
                    - (self.Time[len(self.loadtxt) - 1] // 360) * 60
                )
                + "分"
            )
