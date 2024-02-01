from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class listService(BaseService):
    def get_code(self):
        return "list"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        for element in self.file.content:
            print(element)
