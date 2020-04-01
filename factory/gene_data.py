import os
from xeger import Xeger
import shutil
import random

from reg_exp import RegExp


def get_id_list():
    id_list = []
    for i in range(random.randint(1, 30)):
        id = random.randint(1, 150)
        while id in id_list:
            id = random.randint(1, 150)
        id_list.append(id)
    random.shuffle(id_list)
    return id_list


def set_put_time(id_list=[]):
    time_cnt = len(id_list)
    time_list = []  # contains float type time
    new_time_list = []  # contains string type time
    start_time = random.random() * 5
    end_time = random.random() * 40
    while (end_time <= start_time):
        end_time = random.random() * 40
    if (end_time < 30):
        end_time += 10
    time_list.append(start_time)
    time_list.append(end_time)
    for i in range(time_cnt - 2):
        time_list.append(random.uniform(start_time, end_time))
    time_list.sort()
    for time in time_list:
        dot_pos = str(time).index('.')
        new_time_list.append(str(time)[:dot_pos + 2])
    return new_time_list


def get_req_list():
    req_list = []
    id_list = get_id_list()
    time_list = set_put_time(id_list)
    for i in range(len(id_list)):
        from_floor = random.randint(1, 15)
        while (from_floor == 0):
            from_floor = random.randint(1, 15)
        to_floor = random.randint(1, 15)
        while (to_floor == 0):
            to_floor = random.randint(1, 15)
        while from_floor == to_floor:
            to_floor = random.randint(1, 15)
        req_list.append("[" + time_list[i] + "]" + str(id_list[i]) + "-FROM-" +
                        str(from_floor) + "-TO-" + str(to_floor) + "\n")
    return req_list


def gene_data(case_count=10):
    if (os.path.exists("./data")):
        shutil.rmtree("./data")
    os.mkdir("./data")
    for i in range(case_count):
        with open("./data/testcase" + str(i) + ".txt", 'w') as f:
            data = get_req_list()
            f.writelines(data)


if __name__ == "__main__":
    gene_data()
