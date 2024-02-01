from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class AppendHeadService(BaseService):
    To_AppendHead = []

    def get_code(self):
        return "append-head"

    def get_category(self):
        return Category.modify

    def process(self, data):
        # append-head # 新的标题
        data = data.split(" ", 1)  # 这里把 append-head # 新的标题分成两块

        if len(data) < 2:
            raise Exception("参数格式错误")
        self.To_AppendHead.append(data)
        self.file.content.insert(0, data[1])
        self.file.fileworkspace[self.file.file_workspace] = 1

    def undo(self):
        self.file.content.pop(0)

    def redo(self):
        self.process(
            "".join(
                ["append-head ", self.To_AppendHead[len(self.To_AppendHead) - 1][1]]
            )
        )
        self.To_AppendHead.pop()
