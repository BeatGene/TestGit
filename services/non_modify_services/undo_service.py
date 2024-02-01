from services.base_service import BaseService
from Common.Constant.Category import Category
from services.non_modify_services.redo_service import RedoService


# 没问题
class UndoService(BaseService):
    undo_list = []

    def get_code(self):
        return "undo"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        if not UndoService.undo_list:
            # print(self.file.content)
            return
        service = UndoService.undo_list.pop()
        service.undo()
        RedoService.add(service)
        self.file.fileworkspace[self.file.file_workspace] = 1

    @classmethod
    def add(self, service):
        UndoService.undo_list.append(service)
