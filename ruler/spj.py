import os
import random
import shutil
import time
from subprocess import PIPE, Popen

from door import door_check
from move import move_check
from output_parser import get_state
from person import person_check
from time_judge import time_check


# list of original input
def get_input_list(data_file):
    input_list = []
    with open(data_file, 'r') as f_in:
        tmp_input_list = f_in.readlines()
        for req in tmp_input_list:
            req = req.strip('\n')
            try:
                pos = req.index(']')
                req = req[pos + 1:]
            except ValueError:
                pass
            if (req == ""):
                continue
            input_list.append(req)
    return input_list


# list of original output
def get_output_list(output_file):
    output_list = []
    with open(output_file, 'r') as f_out:
        tmp_output_list = f_out.readlines()
        for output in tmp_output_list:
            output = output.strip('\n')
            output_list.append(output)
    return output_list


# list of timed arrive
def get_arrive_list(output_list=[]):
    arrive_list = []
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if (state_i == "ARRIVE"):
            arrive_list.append(output_list[i])
    return arrive_list


# list of timed OPEN/CLOSE
def get_door_list(output_list=[]):
    door_list = []
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if (state_i == "OPEN" or state_i == "CLOSE"):
            door_list.append(output_list[i])
    return door_list


# list of strip-time IN/OUT
def get_send_list(output_list=[]):
    send_list = []
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if (state_i == "IN" or state_i == "OUT"):
            pos = (int)((output_list[i]).index(']') + 1)
            send_list.append(output_list[i][pos:])
    return send_list


def check(data_file, output_file):
    input_list = get_input_list(data_file)
    output_list = get_output_list(output_file)
    arrive_list = get_arrive_list(output_list)
    door_list = get_door_list(output_list)
    send_list = get_send_list(output_list)

    r1 = door_check(output_list, door_list)
    if (r1 != ""):
        return r1 + " in door_check has problem"
    r2 = move_check(arrive_list)
    if (r2 != ""):
        return r2 + " in move_check has problem"
    r3 = person_check(input_list, output_list, send_list)
    if (r3 != ""):
        return r3 + " in person_check has problem"
    r4 = time_check(data_file, output_file)
    if (r4):
        return "time_check has problem"

    return ""


if __name__ == "__main__":
    r = check("./data/testcase0.txt", "./output/archer/output0.txt")
    print(r)
