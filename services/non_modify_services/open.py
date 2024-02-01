from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class listService(BaseService):
    filenameTemp = -1

    def get_code(self):
        return "switch"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        # open 文件名
        data = data.split(" ", 1)  # 这里把 open 文件名 分成两块

        if len(data) < 2:
            raise Exception("参数格式错误")
        else:
            self.file.file_workspace = int(data[1]) - 1
            self.file.content = self.file.filecontent[self.file.file_workspace]
