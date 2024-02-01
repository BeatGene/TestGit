from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class DeleteService(BaseService):
    To_Insert = []
    To_Insert_Num = []
    final = 0
    To_Delete = []

    def get_code(self):
        return "delete"

    def get_category(self):
        return Category.modify

    def process(self, data):
        # delete 文本 或者delete 行号
        data = data.split(" ", 1)  # 这里把delete 文本分成两块
        if len(data) < 2:
            raise Exception("参数格式错误")
        self.To_Delete.append(data)
        if data[1].isdigit():
            self.To_Insert_Num.append(int(data[1]) - 1)
            self.To_Insert.append(self.file.content[int(data[1]) - 1])
            self.file.content.pop(int(data[1]) - 1)
        else:
            for i in range(0, len(self.file.content)):
                if data[1] in self.file.content[i]:
                    self.To_Insert_Num.insert(len(self.To_Insert_Num), i)
                    self.To_Insert.insert(len(self.To_Insert), self.file.content[i])
                    self.final = i
                    break
            self.file.content.pop(self.final)
            self.file.fileworkspace[self.file.file_workspace] = 1

    def undo(self):
        self.file.content.insert(
            self.To_Insert_Num[len(self.To_Insert_Num) - 1],
            self.To_Insert[len(self.To_Insert) - 1],
        )
        self.To_Insert_Num.pop()
        self.To_Insert.pop()

    def redo(self):
        self.process("".join(["delete ", self.To_Delete[len(self.To_Delete) - 1][1]]))
        self.To_Delete.pop()
