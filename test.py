# 自动测试用例
from handler.executor import Executor
from Domain.File import File
import unittest


class Test(unittest.TestCase):
    def test_executor(self):
        executor_test = Executor()
        file = File()
        executor_test.execute("append-head # 新的标题")
        self.assertEqual(file.content[0], "# 新的标题")

        executor_test.execute("append-tail # 子标题")
        self.assertEqual(file.content[-1], "# 子标题")

        executor_test.execute("delete 1")
        self.assertNotEqual(file.content[0], "# 新的标题")

        executor_test.execute("insert 1 ## 新的文本")
        self.assertEqual(file.content[0], "## 新的文本")


if __name__ == "__main__":
    unittest.main()
