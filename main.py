from handler.executor import Executor
from services.modify_services.load_service import LoadsService
import time

if __name__ == "__main__":
    Str_Session = "Session.md"
    f = open("Session.md", "a")
    f.write("session start at" + " " + str(time.asctime()) + "\n")
    f.close()
    executor = Executor()
    LoadsService.init(LoadsService)
    while True:
        executor.execute(input())
