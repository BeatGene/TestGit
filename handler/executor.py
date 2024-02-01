from services.non_modify_services.undo_service import UndoService
from services.non_modify_services.history_service import HistoryService
from Common.Utils.Exception import exception_wrapper
from Common.Constant.Category import Category
from handler.router import Router
import time


class Executor(object):
    def __init__(self):
        self.router = Router()

    @exception_wrapper()
    def execute(self, string):
        params = string.split()
        target_service = self.router.find_route(params[0])()
        HistoryService.operate_list.append(string)
        HistoryService.operate_time_list.append(time.asctime())
        target_service.process(string)

        if target_service.get_category() == Category.modify:
            UndoService.add(target_service)
