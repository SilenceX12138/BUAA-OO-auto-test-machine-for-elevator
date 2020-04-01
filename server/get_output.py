import os
import shutil
import time
from random import random
from subprocess import PIPE, Popen


def get_time_and_req_list(data_list=[]):
    time_list = []
    req_list = []
    for data in data_list:
        sep_pos = ((str)(data)).index(']')
        time_list.append(data[1:sep_pos - 2])
        req_list.append(data[sep_pos - 1:])
    return time_list, req_list


def get_delay_time_list(time_list=[]):
    delay_time_list = []
    prev = 0.0
    for time in time_list:
        tmp_delay_time = (float)(time) - prev
        delay_time_list.append(tmp_delay_time)
        prev = (float)(time)
    return delay_time_list


def get_output(dirname, datadir):
    output_path = "./output/" + dirname
    if (os.path.exists(output_path)):
        shutil.rmtree(output_path)
    os.mkdir(output_path)
    case_count = len(os.listdir(datadir))
    class_path = "./lib/" + dirname
    for i in range(case_count):
        with open(datadir + "/testcase" + str(i) + ".txt", 'rb') as f_in:
            data_list = f_in.readlines()
            time_list, req_list = get_time_and_req_list(data_list)
            delay_time_list = get_delay_time_list(time_list)
        jvm_start_time = time.time()
        with open(output_path + "/output" + str(i) + ".txt", 'w') as f_out:
            elev_proc = Popen(
                r'java -jar ' + class_path + '/2-1.jar',
                stdin=PIPE,
                stdout=f_out,
            )
        jvm_launch_time = time.time() - jvm_start_time
        for i in range(len(data_list)):
            delay_time = abs(delay_time_list[i] - jvm_launch_time)
            time.sleep(delay_time)
            elev_proc.stdin.write(req_list[i])
            elev_proc.stdin.flush()
    elev_proc.communicate()


if __name__ == "__main__":
    get_output("archer", "./data")
