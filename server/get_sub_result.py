import os
import shutil
import sys
import threading
import time

from subprocess import Popen, PIPE

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "/ruler")

from get_output import get_output
from spj import check


class get_sub_result(threading.Thread):
    def __init__(self, dirname, datadir):
        threading.Thread.__init__(self)
        self.dirname = dirname
        self.datadir = datadir

    def run(self):
        ''' evaluate time on Linux '''
        '''
        r = Popen("time python ./server/get_output.py " + self.dirname + " " +
                  self.datadir,
                  stderr=PIPE,
                  shell=True)
        s = str(r.stderr.read()).replace('\'', '')[1:]
        usr_time = float(s.split(' ')[0][:-4])
        sys_time = float(s.split(' ')[1][:-6])
        cpu_time = sys_time + usr_time
        self.check_result(cpu_time)
        # print(usr_time)
        # print(sys_time)
        '''
        ''' evaluate correction '''
        get_output(self.dirname, self.datadir)
        self.check_result()

    def check_result(self, cpu_time=0):
        result_path = "./result/" + self.dirname
        if (os.path.exists(result_path)):
            shutil.rmtree(result_path)
        os.mkdir(result_path)
        data_cnt = os.listdir(self.datadir)
        with open("./result/" + self.dirname + "/result.txt", "w") as f_rst:
            for i in range(len(data_cnt)):
                data_file = self.datadir + "/" + "testcase" + str(i) + ".txt"
                try:
                    r = check(
                        data_file, "./output/" + self.dirname + "/output" +
                        str(i) + ".txt")
                except (Exception, ValueError):
                    r = "unexpected situation occured!"
                if (r != "" or cpu_time >= 10 - 0.000001):
                    try:
                        shutil.copyfile(
                            data_file,
                            "./download_data/" + "testcase" + str(i) + ".txt")
                    except Exception:
                        pass
                    f_rst.writelines("----------Testcase" + str(i) +
                                     "----------\n")
                    f_rst.writelines(r + "\nCPU TIME: " + str(cpu_time) +
                                     "\n\n")
            f_rst.writelines("Finished\n")


if __name__ == "__main__":
    r = get_sub_result("archer", "./data")
    r.run()