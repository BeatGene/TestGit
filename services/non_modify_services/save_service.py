from services.base_service import BaseService
from Common.Constant.Category import Category
from services.non_modify_services.stats_service import statsService


# 没问题
class SaveService(BaseService):
    def get_code(self):
        return "save"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        # save ⽂件
        self.file.fileworkspace[self.file.file_workspace] = 0
        f = open(self.file.filename[self.file.file_workspace], "w")
        for line in self.file.content:
            f.write(line + "\n")
        f.close()
        Str_Session = "Session.md"
        f = open(Str_Session, "a")
        if len(statsService.loadtxt) > 0 and len(statsService.Time) > 0:
            f.write(
                str(statsService.loadtxt[-1])
                + " "
                + str(statsService.Time[-1] // 360)
                + "时"
                + str(
                    (statsService.Time[-1] // 60 - (statsService.Time[-1] // 360) * 60)
                )
                + "分"
                + "\n"
            )
        f.close()  # 写入日志
