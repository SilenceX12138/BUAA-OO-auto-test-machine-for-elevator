from output_parser import get_floor, get_state, get_time, get_send_info
from request_parser import get_req_info

# door should be open when (un)load person -> only OPEN/IN/OUT can be ahead of IN/OUT


def in_and_out_on_open_judge(output_list=[]):
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if(state_i == "IN" or state_i == "OUT"):
            if(i == 0):
                return True
            j = i-1
            state_j = get_state(j, output_list)
            if(state_j != "OPEN" and state_j != "IN" and state_j != "OUT"):
                return True
    return False

# all people should arrive at dest finally
# -> req_in and req_out can be found in send_list and req_in is ahead of req_out


def dest_judge(input_list=[], send_list=[]):
    for req in input_list:
        req_id, from_floor, to_floor = get_req_info(req)
        req_in = "IN-"+str(req_id)+"-"+str(from_floor)
        req_out = "OUT-"+str(req_id)+"-"+str(to_floor)
        in_pos = [index for (index, value) in enumerate(
            send_list) if value == req_in]
        out_pos = [index for (index, value) in enumerate(
            send_list) if value == req_out]
        if(len(in_pos) == 1 and len(out_pos) == 1 and in_pos[0] < out_pos[0]):
            continue
        return True
    return False

# person (un)loading should be at the floor elevator opens
# -> within a pair of IN/OUT floor stays the same


def meet_floor_judge(output_list=[]):
    for i in range(len(output_list)):
        state_i = get_state(i, output_list)
        if(state_i == "OPEN"):
            std_floor = get_floor(i, output_list)
            for j in range(i+1, len(output_list)):
                state_j = get_state(j, output_list)
                if(state_j == "CLOSE"):
                    break
            for output in output_list[i+1:j]:
                pos = output.index(']')
                send = output[pos+1:]
                state, send_id, floor = get_send_info(send)
                if(floor != std_floor):
                    return True

    return False


def person_check(input_list=[], output_list=[], send_list=[]):
    r1 = dest_judge(input_list, send_list)
    if(r1):
        return "1"
    r2 = in_and_out_on_open_judge(output_list)
    if(r2):
        return "2"
    r3 = meet_floor_judge(output_list)
    if(r3):
        return "3"
    return ""


if __name__ == "__main__":
    r = in_and_out_on_open_judge(['[   0.4780]ARRIVE-2', '[   0.8840]OPEN-2', '[   0.8840]IN-3-2', '[   1.2840]CLOSE-2', '[   1.2840]ARRIVE-3', '[   1.6880]OPEN-3', '[   1.6880]OUT-3-3', '[   2.0920]CLOSE-3',
                                  '[   3.7180]ARRIVE-2', '[   4.1190]ARRIVE-1', '[   4.5230]OPEN-1', '[   4.5250]IN-1-1', '[   4.9290]CLOSE-1', '[   4.9310]ARRIVE-2', '[   5.3330]OPEN-2', '[   5.3350]OUT-1-2', '[   5.7380]CLOSE-2'])
    print(r)
