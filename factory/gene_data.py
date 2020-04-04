import os
import random
import shutil

from xeger import Xeger

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
    start_time = random.random() * 4 + 1  #[1,5]
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
        from_floor, to_floor = get_from_and_to()
        req_list.append("[" + time_list[i] + "]" + str(id_list[i]) + "-FROM-" +
                        str(from_floor) + "-TO-" + str(to_floor) + "\n")
    return req_list


def get_from_and_to():
    seed = random.randint(1, 100)
    if (seed <= 15):
        return all_neg_data()
    elif (seed <= 25):
        return all_pos_data()
    elif (seed <= 40):
        return neg_to_pos_data()
    elif (seed <= 55):
        return pos_to_neg_data()
    elif (seed <= 70):
        return edge_start_data()
    elif (seed <= 85):
        return edge_end_data()
    elif (seed <= 100):
        return edge_to_edge_data()


def all_neg_data():
    from_floor = random.randint(-3, -1)
    to_floor = random.randint(-3, -1)
    while from_floor == to_floor:
        to_floor = random.randint(-3, -1)
    return from_floor, to_floor


def all_pos_data():
    from_floor = random.randint(1, 16)
    to_floor = random.randint(1, 16)
    while from_floor == to_floor:
        to_floor = random.randint(1, 16)
    return from_floor, to_floor


def neg_to_pos_data():
    from_floor = random.randint(-3, -1)
    to_floor = random.randint(1, 16)
    return from_floor, to_floor


def pos_to_neg_data():
    from_floor = random.randint(1, 16)
    to_floor = random.randint(-3, -1)
    return from_floor, to_floor


def edge_start_data():
    edge = [-3, -1, 1, 16]
    from_floor = random.choice(edge)
    to_floor = random.randint(-3, 16)
    while (to_floor == 0 or to_floor == from_floor):
        to_floor = random.randint(-3, 16)
    return from_floor, to_floor


def edge_end_data():
    edge = [-3, -1, 1, 16]
    from_floor = random.randint(-3, 16)
    while (from_floor == 0):
        from_floor = random.randint(-3, 16)
    to_floor = random.choice(edge)
    while (to_floor == from_floor):
        to_floor = random.choice(edge)
    return from_floor, to_floor


def edge_to_edge_data():
    edge = [-3, -1, 1, 16]
    from_floor = random.choice(edge)
    to_floor = random.choice(edge)
    while from_floor == to_floor:
        to_floor = random.choice(edge)
    return from_floor, to_floor


def gene_data(case_count=10):
    if (os.path.exists("./data")):
        shutil.rmtree("./data")
    os.mkdir("./data")
    for i in range(case_count):
        with open("./data/testcase" + str(i) + ".txt", 'w') as f:
            f.writelines("[0.0]" + str(random.randint(1, 5)) + "\n")
            data = get_req_list()
            f.writelines(data)


if __name__ == "__main__":
    gene_data()
