from services.base_service import BaseService
from Common.Constant.Category import Category


# 没问题
class InsertService(BaseService):
    To_delete_Num = []
    To_Insert = []

    def get_code(self):
        return "insert"

    def get_category(self):
        return Category.modify

    def process(self, data):
        # insert [⾏号] 标题/⽂本
        data = data.split(" ", 2)  # 这里把 insert [⾏号] 标题/⽂本 分成三块
        if len(data) < 2:
            raise Exception("参数格式错误")
        self.To_Insert.append(data)
        if data[1].isdigit():
            self.To_delete_Num.insert(len(self.To_delete_Num), int(data[1]) - 1)
            self.file.content.insert(int(data[1]) - 1, data[2])
        else:
            self.file.content.insert(len(self.file.content), data[1] + " " + data[2])
            self.To_delete_Num.insert(
                len(self.To_delete_Num), len(self.file.content) - 1
            )
        self.file.fileworkspace[self.file.file_workspace] = 1

    def undo(self):
        self.file.content.pop(self.To_delete_Num[len(self.To_delete_Num) - 1])
        self.To_delete_Num.pop()

    def redo(self):
        self.process(
            "".join(
                [
                    "insert",
                    " ",
                    self.To_Insert[len(self.To_Insert) - 1][1],
                    " ",
                    self.To_Insert[len(self.To_Insert) - 1][2],
                ]
            )
        )
        self.To_Insert.pop()
