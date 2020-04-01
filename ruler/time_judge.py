import os
import shutil
import sys


def get_std_time(datadir):
    if (os.path.exists("./ruler/std-time")):
        shutil.rmtree("./ruler/std-time")
    os.mkdir("./ruler/std-time")
    data_cnt = len(os.listdir(datadir))
    for i in range(data_cnt):
        data_file = datadir + "/testcase" + str(i) + ".txt"
        time_file = "./ruler/std-time/time" + str(i) + ".txt"
        os.system(r"ruler\datacheck_win.exe -i " + data_file + " > " +
                  time_file)


def time_check(data_file, output_file):
    with open(output_file, 'r') as f_opt:
        output = f_opt.readlines()[-1]
        pos = output.index(']')
        real_time = (float)(output[1:pos])

    case_pos = data_file.index('testcase')
    dot_pos = data_file.index('.txt')
    i = data_file[case_pos + 8:dot_pos]

    with open("./ruler/std-time/time" + str(i) + ".txt", "r") as f_std:
        time_limit = (int)(f_std.readline().split(' ')[-1])

    if (real_time >= time_limit):
        return True
    return False


if __name__ == "__main__":
    r = time_check("./data/testcase0.txt", "./output/altergo/output0.txt")
    print(r)
