import re


def get_state(i, elevtor_list=[]):
    pos_i1 = int(elevtor_list[i].index(']') + 1)
    pos_i2 = int(elevtor_list[i].index('-'))
    state_i = elevtor_list[i][pos_i1:pos_i2]
    return state_i


def get_time(i, elevtor_list=[]):
    pos_i = (int)(elevtor_list[i].index(']'))
    time_i = (float)(elevtor_list[i][1:pos_i])
    return time_i


def get_floor(i, elevator_list=[]):
    pos_i = (int)(elevator_list[i].index('-')) + 1
    floor_i = (int)(elevator_list[i][pos_i:])
    return floor_i


def get_send_info(send=""):
    pos = send.index('-')
    state = send[:pos]
    send = send[pos+1:]
    pos = send[1:].index('-')+1
    id = send[:pos]
    floor = send[pos+1:]
    # IN or OUT, id, floor
    return str(state), int(id), int(floor)
