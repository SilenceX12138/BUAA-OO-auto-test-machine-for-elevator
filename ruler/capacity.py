from output_parser import get_state


def capacity_check(send_list=[], elev_type=''):
    if (elev_type == 'A'):
        in_str = "1111111"
    elif (elev_type == 'B'):
        in_str = "111111111"
    elif (elev_type == 'C'):
        in_str = "11111111"

    state_str = ""
    for send in send_list:
        state = get_state(0,[send])
        if (state == "IN"):
            state_str += "1"
        else:
            state_str += "0"

    if (in_str in state_str):
        return True
    return False


if __name__ == "__main__":
    r = capacity_check([
        'IN-15', 'OUT-15', 'IN-15', 'OUT-15', 'IN-15', 'IN-15', 'IN-15',
        'IN-15', 'IN-15', 'IN-15', 'IN-15'
    ], 'C')

    print(r)
