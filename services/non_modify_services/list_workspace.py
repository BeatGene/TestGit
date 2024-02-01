from services.base_service import BaseService
from Common.Constant.Category import Category


class list_workspace(BaseService):
    def get_code(self):
        return "ws"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        for i in range(0, len(self.file.filename)):
            if i == self.file.file_workspace:
                print(
                    str(i + 1)
                    + " "
                    + self.file.filename[i]
                    + "*" * self.file.fileworkspace[i]
                    + "<"
                )
            else:
                print(
                    str(i + 1)
                    + " "
                    + self.file.filename[i]
                    + "*" * self.file.fileworkspace[i]
                )
