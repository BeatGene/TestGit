from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class dir_treeService(BaseService):
    def get_code(self):
        return "dir-tree"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        self.file.Caculate()
        Mun = 0
        data = data.split(" ", 1)
        for i in range(0, len(self.file.content)):
            if data[1] in self.file.content[i]:
                Mun = i
                break
        for i in range(Mun, len(self.file.content)):
            data_new = self.file.content[i].split(" ", 1)
            print(self.file.content_num[i] * "  " + "└──" + data_new[1])
