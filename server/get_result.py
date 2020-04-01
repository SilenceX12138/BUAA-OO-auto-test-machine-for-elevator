import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "/ruler")

from get_sub_result import get_sub_result
from time_judge import get_std_time


def get_result(datadir):
    dirnames = os.listdir("./lib")
    threads = []
    get_std_time(datadir)
    for dirname in dirnames:
        thread = get_sub_result(dirname, datadir)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    with open("./summary/digit/spj_result.txt", 'w') as f_rst:
        for dirname in dirnames:
            result_file = "./result/" + dirname + "/result.txt"
            with open(result_file, 'r') as f_sub_rst:
                r = f_sub_rst.readlines()
                if (len(r) > 1):
                    f_rst.write(dirname + " needs help\n")
        f_rst.write("Finished\n")


if __name__ == "__main__":
    get_result("./data")
