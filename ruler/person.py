from output_parser import get_state, get_time, get_send_info, get_send_floor, get_door_floor
from request_parser import get_req_info


# door should be open when (un)load person -> only OPEN/IN/OUT can be ahead of IN/OUT
def in_and_out_on_open_judge(output_list=[]):
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if (state_i == "IN" or state_i == "OUT"):
            if (i == 0):
                return True
            j = i - 1
            state_j = get_state(j, output_list)
            if (state_j != "OPEN" and state_j != "IN" and state_j != "OUT"):
                return True
    return False


# all people should arrive at dest finally
# -> req_in and req_out can be found in send_list and req_in is ahead of req_out
def dest_judge(input_list=[], send_list=[]):
    for req in input_list:
        req_id, from_floor, to_floor = get_req_info(req)
        req_in = "IN-" + str(req_id) + "-" + str(from_floor)
        req_out = "OUT-" + str(req_id) + "-" + str(to_floor)
        in_pos = [
            index for (index, value) in enumerate(send_list) if value == req_in
        ]
        out_pos = [
            index for (index, value) in enumerate(send_list)
            if value == req_out
        ]
        if (len(in_pos) == 1 and len(out_pos) == 1 and in_pos[0] < out_pos[0]):
            continue
        return True
    return False


# person (un)loading should be at the floor elevator opens
# -> within a pair of IN/OUT floor stays the same
def meet_floor_judge(output_list=[]):
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if (state_i == "OPEN"):
            std_floor = get_door_floor(i, output_list)
            for j in range(i + 1, len(output_list)):
                state_j = get_state(j, output_list)
                if (state_j == "CLOSE"):
                    break
            for output in output_list[i + 1:j]:
                pos = output.index(']')
                send = output[pos + 1:]
                state, send_id, floor = get_send_info(send)
                if (floor != std_floor):
                    return True
    return False


# every transfer should have a SUB dest_judge
# -> adjacent (OUT after IN) should occur on ONE floor
def transfer_judge(id_send_dic=[]):
    for id, sub_send_list in id_send_dic.items():
        if (len(sub_send_list) % 2 != 0):
            return True
        if (get_state(0, sub_send_list) != "IN"):
            return True
        for i in range(1, len(sub_send_list) - 1):
            if (i % 2 == 0):
                continue
            out_one = sub_send_list[i]
            in_two = sub_send_list[i + 1]
            state_one = get_state(i, sub_send_list)
            state_two = get_state(i + 1, sub_send_list)
            if (state_one != "OUT" or state_two != "IN"):
                return True
            floor_one = get_send_floor(i, sub_send_list)
            floor_two = get_send_floor(i + 1, sub_send_list)
            if (floor_one != floor_two):
                return True
    return False


def person_check(output_list=[], send_list=[], id_send_dic={}):
    r1 = in_and_out_on_open_judge(output_list)
    if (r1):
        return "1"
    r1 = meet_floor_judge(output_list)
    if (r1):
        return "2"
    return ""


if __name__ == "__main__":
    r = transfer_judge({'A': ["OUT-1-1", "OUT-1--2", "IN-1--2", "OUT-1-1"]})
    print(r)
