from services.base_service import BaseService
from Common.Constant.Category import Category
from services.non_modify_services.stats_service import statsService


class CloseService(BaseService):
    def get_code(self):
        return "close"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        data = data.split(" ", 1)
        if self.file.fileworkspace[int(data[1]) - 1] == 0:
            self.file.filename.pop(int(data[1]) - 1)
            self.file.fileworkspace.pop(int(data[1]) - 1)
            self.file.filecontent.pop(int(data[1]) - 1)
        else:
            a = ""
            a = input("save changed file before closing?[y/n]")
            if a == "n":
                self.file.filename.pop(int(data[1]) - 1)
                self.file.fileworkspace.pop(int(data[1]) - 1)
                self.file.filecontent.pop(int(data[1]) - 1)
            else:
                f = open(self.file.filename[int(data[1]) - 1], "w")
                for line in self.file.filecontent[int(data[1]) - 1]:
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
                            (
                                statsService.Time[-1] // 60
                                - (statsService.Time[-1] // 360) * 60
                            )
                        )
                        + "分"
                        + "\n"
                    )
                f.close()
                self.file.filename.pop(int(data[1]) - 1)
                self.file.fileworkspace.pop(int(data[1]) - 1)
                self.file.filecontent.pop(int(data[1]) - 1)
