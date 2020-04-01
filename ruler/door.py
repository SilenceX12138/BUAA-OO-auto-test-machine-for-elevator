from output_parser import get_floor, get_state, get_time

# open and close can only occur after the other occurs


def open_and_close_judge(door_list=[]):
    for i in range(len(door_list)-1):
        j = i+1
        state_i = get_state(i, door_list)
        state_j = get_state(j, door_list)
        if(state_i == state_j):
            return True
    return False

# open can only occur when elevator stops -> only ARRIVE/CLOSE/NOP can be ahead of OPEN


def open_on_arrive_judge(output_list=[]):
    for i in range(1, len(output_list)):
        state_i = get_state(i, output_list)
        if(state_i == "OPEN"):
            j = i-1
            state_j = get_state(j, output_list)
            if(state_j != "ARRIVE"and state_j != "CLOSE"):
                return True
    return False

# elevator can only move after door is closed -> only ARRIVE and CLOSE can be ahead of ARRIVE


def arrive_on_close_judge(output_list=[]):
    for i in range(1, len(output_list)):
        state_i = get_state(i, output_list)
        if(state_i == "ARRIVE"):
            j = i-1
            state_j = get_state(j, output_list)
            if(state_j != "ARRIVE" and state_j != "CLOSE"):
                return True
    return False

# interval between a pair of OPEN and CLOSE should be no less than 0.4s
# and the floor of a pair needs to be equivalent


def open_time_and_floor_judge(door_list=[]):
    for i in range(len(door_list)-1):
        if(i % 2 != 0):  # OPEN must be at even pos
            continue
        j = i+1
        time_i = get_time(i, door_list)
        time_j = get_time(j, door_list)
        if(not(time_j-time_i >= (0.4-0.00000001))):
            return True
        floor_i = get_floor(i, door_list)
        floor_j = get_floor(j, door_list)
        if(floor_i != floor_j):
            return True
    return False

# door must be closed finally -> the length of door_list is even with open_and_close_judge satisfied


def close_on_finish_judge(door_list=[]):
    if(len(door_list) % 2 != 0):
        return True
    return False


def door_check(output_list=[], door_list=[]):
    r1 = arrive_on_close_judge(output_list)
    if(r1):
        return "1"
    r2 = close_on_finish_judge(door_list)
    if(r2):
        return "2"
    r3 = open_and_close_judge(door_list)
    if(r3):
        return "3"
    r4 = open_on_arrive_judge(output_list)
    if(r4):
        return "4"
    r5 = open_time_and_floor_judge(door_list)
    if(r5):
        return "5"
    return ""


if __name__ == "__main__":
    r = open_time_and_floor_judge(
        ['[4.3001]OPEN-13', '[4.7002]OPEN-13', '[5.004]OPEN-1'])
    print(r)
