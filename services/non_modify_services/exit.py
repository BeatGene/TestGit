from services.base_service import BaseService
from Common.Constant.Category import Category
from services.non_modify_services.stats_service import statsService
import sys


class ExitService(BaseService):
    Temp = 0

    def chucun(self):
        TempList = []
        TempList.append(str(self.file.file_workspace))
        for i in range(0, len(self.file.filename)):
            TempList.append(self.file.filename[i])
        f = open("Temp.md", "w")
        for line in TempList:
            f.write(line + "\n")
        f.close()

    def get_code(self):
        return "exit"

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        for i in range(0, len(self.file.filename)):
            if self.file.fileworkspace[i] == 1:
                self.Temp = 1
                break
        if self.Temp == 0:
            self.chucun()
            sys.exit(0)
        else:
            b = ""
            b = input("Do you want to save the unsaved workspace [Y/N] ?")
            if b == "N":
                self.chucun()
                sys.exit(0)
            else:
                for i in range(0, len(self.file.filename)):
                    if self.file.fileworkspace[i] == 1:
                        self.file.file_workspace = i
                        self.file.content = self.file.filecontent[i]
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
                                    (
                                        statsService.Time[-1] // 60
                                        - (statsService.Time[-1] // 360) * 60
                                    )
                                )
                                + "分"
                                + "\n"
                            )
                        f.close()
                self.chucun()
                sys.exit(0)
