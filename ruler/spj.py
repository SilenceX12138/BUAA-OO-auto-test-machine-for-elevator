import os
import random
import shutil
import time
from subprocess import PIPE, Popen

from door import door_check
from move import move_check
from output_parser import get_state
from person import person_check, dest_judge, transfer_judge
from time_judge import time_check
from capacity import capacity_check


# list of strip-time input
def get_input_list(data_file):
    input_list = []
    elev_type_dic = {}
    with open(data_file, 'r') as f_in:
        tmp_input_list = f_in.readlines()
        for req in tmp_input_list:
            req = req.strip('\n')
            if (']' in req):
                pos = req.index(']')
                req = req[pos + 1:]
            if (len(req) <= 1):
                continue
            if ('X' in req):  # add elevator command: [1.0]X1-ADD-ELEVATOR-B
                tag = req[0:2]  # name of elevator: X1/X2/X3
                elev_type = req[-1]
                elev_type_dic[tag] = elev_type
            else:
                input_list.append(req)  # only add non-add command
    return input_list, elev_type_dic


# list of timed but strip-elev output
def get_output_list(output_file):
    output_list = []
    sub_output_lists = {}
    with open(output_file, 'r') as f_out:
        tmp_output_list = f_out.readlines()
        for output in tmp_output_list:
            output = output.strip('\n')
            if ('X' in output):
                tag = output[-2:]
                output_list.append(output[:-3])
            else:
                tag = output[-1]

                output_list.append(output[:-2])
            if (tag in sub_output_lists):
                if ('X' in tag):
                    sub_output_lists[tag].append(output[:-3])
                else:
                    sub_output_lists[tag].append(output[:-2])
            else:
                if ('X' in tag):
                    sub_output_lists[tag] = [output[:-3]]
                else:
                    sub_output_lists[tag] = [output[:-2]]
    return output_list, sub_output_lists


# list of timed ARRIVE
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
    id_send_dic = {}
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if (state_i == "IN" or state_i == "OUT"):
            pos = int((output_list[i]).index(']') + 1)
            send_list.append(output_list[i][pos:])
            sep_pos_first = output_list[i].index('-')
            if ("--" in output_list[i]):
                sep_pos_last = output_list[i].rindex('-') - 1
            else:
                sep_pos_last = output_list[i].rindex('-')
            id = int(output_list[i][sep_pos_first + 1:sep_pos_last])
            if (id in id_send_dic):
                id_send_dic[id].append(output_list[i][pos:])
            else:
                id_send_dic[id] = [output_list[i][pos:]]
    return send_list, id_send_dic


def judge(data_file, output_file):
    input_list, elev_type_dic = get_input_list(data_file)
    output_list, sub_output_lists = get_output_list(output_file)
    send_list, id_send_dic = get_send_list(output_list)

    r0 = dest_judge(input_list, send_list) | transfer_judge(id_send_dic)
    if (r0):
        return "dest_judge and transfer_judge has problem"

    for elev in sub_output_lists:
        if ('X' in elev):
            elev_type = elev_type_dic[elev]
        else:
            elev_type = elev
        sub_output_list = sub_output_lists[elev]
        sub_arrive_list = get_arrive_list(sub_output_list)
        sub_door_list = get_door_list(sub_output_list)
        sub_send_list, sub_id_send_dic = get_send_list(sub_output_list)

        r1 = door_check(sub_output_list, sub_door_list, elev_type)
        if (r1 != ""):
            return elev + " : " + r1 + " in door_check has problem"
        r2 = move_check(sub_arrive_list, elev_type)
        if (r2 != ""):
            return elev + " : " + r2 + " in move_check has problem"
        r3 = person_check(sub_output_list, send_list, id_send_dic)
        if (r3 != ""):
            return elev + " : " + r3 + " in person_check has problem"
        r4 = capacity_check(sub_send_list, elev_type)
        if (r4):
            return elev + " : " + "capacity_check has problem"

    return ""


def check(data_file, output_file):
    try:
        return judge(data_file, output_file)
    except (Exception, ValueError):
        return "NOT satisfied"


if __name__ == "__main__":
    r = check("./data/testcase0.txt", "./output/archer/output0.txt")
    print(r)
