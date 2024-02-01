from services.base_service import BaseService
from Common.Constant.Category import Category
import services.non_modify_services.undo_service


# 没问题
class RedoService(BaseService):
    redo_list = []

    def get_code(self):
        return "redo"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        if not self.redo_list:
            # print(self.file.content)
            return
        service = RedoService.redo_list.pop()
        service.redo()
        services.non_modify_services.undo_service.UndoService.add(service)
        self.file.fileworkspace[self.file.file_workspace] = 1

    @classmethod
    def add(self, service):
        RedoService.redo_list.append(service)
