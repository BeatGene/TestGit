from services.base_service import BaseService
from Common.Constant.Category import Category


# 没有显示 不知道为什么 list index out of range
class HistoryService(BaseService):
    operate_list = []
    operate_time_list = []  # 这个列表用来储存每次动作的时间

    def get_code(self):
        return "history"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        # data一般是 history 4的形式
        data = data.split(" ")
        if len(data) < 2:  # 表示没有输入数字或者输入的数字大于list长度  显示全部
            for i in range(0, len(self.operate_list)):
                print(
                    str(self.operate_time_list[len(self.operate_time_list) - i - 1])
                    + " "
                    + str(self.operate_list[len(self.operate_list) - i - 1])
                )
        else:
            if int(data[1]) > len(self.operate_list):
                for i in range(0, len(self.operate_list)):
                    print(
                        str(self.operate_time_list[len(self.operate_time_list) - i - 1])
                        + " "
                        + str(self.operate_list[len(self.operate_list) - i - 1])
                    )
            else:
                for i in range(0, int(data[1])):
                    print(
                        str(self.operate_time_list[len(self.operate_time_list) - i - 1])
                        + " "
                        + str(self.operate_list[len(self.operate_list) - i - 1])
                    )
