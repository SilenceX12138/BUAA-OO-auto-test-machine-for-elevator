import os
import shutil
import stat
import time
import random
import threading
import sys

from subprocess import PIPE, Popen

# add abspath for auto-test-machine
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "/factory")  # / is adaptable to both linux and windows
sys.path.append(path + "/server")

from gene_data import gene_data
from get_result import get_result
from get_graph import get_graph


# build directories needed
def buildcwd():
    dirs_to_build = ['download_data']
    for dir in dirs_to_build:
        if (not os.path.exists("./" + dir)):
            os.mkdir("./" + dir)
    dirs_to_clear = [
        'output', 'result', 'summary', 'summary/digit', 'summary/graph'
    ]
    for dir in dirs_to_clear:
        if (os.path.exists("./" + dir)):
            shutil.rmtree("./" + dir)
        os.mkdir("./" + dir)
    f_rst = open("./summary/digit/spj_result.txt", 'w')
    f_rst.close()


# enumerate and sort testcases when the sequence is chaotic
def enum_and_sort_cases(datapath):
    cases = os.listdir(datapath)
    datas = []
    for case in cases:
        with open(datapath + "/" + case, 'r') as f_case:
            datas.append(f_case.readline())
        os.remove(datapath + "/" + case)
    datas = sorted(datas,
                   key=lambda data: len(data))  # sort is based on length
    for i in range(len(datas)):
        with open(datapath + "/testcase" + str(i) + ".txt", "w") as f_data:
            f_data.write(datas[i])


# whether to perform debug testing
def debug_test():
    print("Do you want to perform debug testing?[y/n] (<Enter> default to y)")
    option = input()
    if (option == 'y' or option == ''):
        return True
    else:
        return False


# whether to perform regression testing
def regression_test():
    print(
        "Do you want to perform regression testing?[y/n] (<Enter> default to y)"
    )
    option = input()
    if (option == 'y' or option == ''):
        return True
    else:
        return False


if __name__ == "__main__":
    os.chdir(path)
    buildcwd()
    if (debug_test()):
        enum_and_sort_cases("./download_data")
        get_result("./download_data")
    elif (regression_test()):
        get_result("./data")
    else:
        gene_data(10)
        get_result("./data")
    get_graph()
