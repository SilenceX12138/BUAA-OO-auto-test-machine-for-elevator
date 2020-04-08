import re


def get_state(i, elevtor_list=[]):
    pos_i1 = 0
    if (']' in elevtor_list[i]):  # parse both timed or strip-time list
        pos_i1 = int(elevtor_list[i].index(']') + 1)
    pos_i2 = int(elevtor_list[i].index('-'))
    state_i = elevtor_list[i][pos_i1:pos_i2]
    return state_i


def get_time(i, elevtor_list=[]):
    pos_i = (int)(elevtor_list[i].index(']'))
    time_i = (float)(elevtor_list[i][1:pos_i])
    return time_i


def get_send_floor(i, elevator_list=[]):
    if ("--" not in elevator_list[i]):
        pos_i = int(elevator_list[i].rindex('-')) + 1
    else:
        pos_i = int(elevator_list[i].rindex('-'))
    floor_i = int(elevator_list[i][pos_i:])
    return floor_i


def get_door_floor(i, elevator_list=[]):
    pos_i = int(elevator_list[i].index('-')) + 1
    floor_i = int(elevator_list[i][pos_i:])
    return floor_i


def get_send_info(send=""):
    pos = send.index('-')
    state = send[:pos]
    send = send[pos + 1:]
    pos = send[1:].index('-') + 1
    id = send[:pos]
    floor = send[pos + 1:]
    # IN or OUT, id, floor
    return str(state), int(id), int(floor)


def get_strip_time_list(elevator_list=[]):
    strip_time_elevator_list = []
    for data in elevator_list:
        pos = 0
        if (']' in data):
            pos = data.index(']') + 1
        data = data[pos:]
        strip_time_elevator_list.append(data)
    return strip_time_elevator_list


if __name__ == "__main__":
    f = get_send_floor(0, ["IN-5-19"])
    print(f)