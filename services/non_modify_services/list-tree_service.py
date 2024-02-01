from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class list_treeService(BaseService):
    def get_code(self):
        return "list-tree"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        self.file.Caculate()
        for i in range(0, len(self.file.content)):
            data = self.file.content[i].split(" ", 1)
            print(self.file.content_num[i] * "  " + "└──" + data[1])
