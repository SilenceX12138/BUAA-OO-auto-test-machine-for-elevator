from output_parser import get_state


def capacity_check(send_list=[]):
    state_str = ""
    for send in send_list:
        sep_pos = send.index('-')
        if (send[:sep_pos] == "OPEN"):
            state_str += "1"
        else:
            state_str += "0"
    try:
        state_str.index("1111111")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    r = capacity_check([
        '[  40.4170]OPEN-15', '[  40.8180]CLOSE-15', '[  40.8180]OPEN-15',
        '[  41.2190]CLOSE-15', '[  40.8180]OPEN-15', '[  40.8180]OPEN-15',
        '[  40.8180]OPEN-15', '[  40.8180]OPEN-15', '[  40.8180]OPEN-15',
        '[  40.8180]OPEN-15', '[  40.8180]OPEN-15'
    ])

    print(r)
