import os
import shutil
import threading
import sys

from get_output import get_output

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "/ruler")

from spj import check


class get_sub_result(threading.Thread):
    def __init__(self, dirname, datadir):
        threading.Thread.__init__(self)
        self.dirname = dirname
        self.datadir = datadir

    def run(self):
        get_output(self.dirname, self.datadir)
        self.check_result()

    def check_result(self):
        result_path = "./result/" + self.dirname
        if (os.path.exists(result_path)):
            shutil.rmtree(result_path)
        os.mkdir(result_path)
        data_cnt = os.listdir(self.datadir)
        with open("./result/" + self.dirname + "/result.txt", "w") as f_rst:
            for i in range(len(data_cnt)):
                data_file = self.datadir + "/" + "testcase" + str(i) + ".txt"
                r = check(
                    data_file,
                    "./output/" + self.dirname + "/output" + str(i) + ".txt")
                if (r != ""):
                    shutil.copyfile(
                        data_file,
                        "./download_data/" + "testcase" + str(i) + ".txt")
                    f_rst.writelines("----------Testcase" + str(i) +
                                     "----------\n")
                    f_rst.writelines(r + "\n\n")
            f_rst.writelines("Finished\n")
