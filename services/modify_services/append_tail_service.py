from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class AppendTailService(BaseService):
    To_AppendTail = []

    def get_code(self):
        return "append-tail"

    def get_category(self):
        return Category.modify

    def process(self, data):
        # append-tail * 新的文本
        data = data.split(" ", 1)  # 这里把 append-tail * 新的文本分成两块

        if len(data) < 2:
            raise Exception("参数格式错误")
        self.To_AppendTail.append(data)
        self.file.content.insert(len(self.file.content), data[1])
        self.file.fileworkspace[self.file.file_workspace] = 1

    def undo(self):
        self.file.content.pop()

    def redo(self):
        self.process(
            "".join(
                ["append-tail ", self.To_AppendTail[len(self.To_AppendTail) - 1][1]]
            )
        )
        self.To_AppendTail.pop()
