
# every move of elevator can only be ONE floor
def distance_judge(arrive_list=[]):
    for i in range(len(arrive_list) - 1):
        j = i + 1
        pos_i = arrive_list[i].index('-') + 1
        pos_j = arrive_list[j].index('-') + 1
        floor_i = int(arrive_list[i][pos_i:])
        floor_j = int(arrive_list[j][pos_j:])
        if (abs(floor_i - floor_j) != 1):
            if(floor_i*floor_j != -1):
                return True
    return False


# interval between adjacent floor should be no less than limit
def time_judge(arrive_list=[], elev_type=''):
    for i in range(len(arrive_list) - 1):
        j = i + 1
        pos_i = arrive_list[i].index(']')
        pos_j = arrive_list[j].index(']')
        time_i = float(arrive_list[i][1:pos_i])
        time_j = float(arrive_list[j][1:pos_j])
        if(elev_type == 'A'):
            if (not (time_j - time_i >= (0.4-0.00000001))):
                return True
        if(elev_type == 'B'):
            if (not (time_j - time_i >= (0.5-0.00000001))):
                return True
        if(elev_type == 'C'):
            if (not (time_j - time_i >= (0.6-0.00000001))):
                return True
    return False


# available range is same([-3,-1] plus [1-20]) while stopby range is different
def reach_judge(arrive_list=[]):
    reach = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in range(len(arrive_list)):
        pos_i = arrive_list[i].index('-') + 1
        floor_i = int(arrive_list[i][pos_i:])
        if (floor_i not in reach):
            return True
    return False


def move_check(arrive_list=[],elev_type = ''):
    r1 = distance_judge(arrive_list)
    if(r1):
        return "1"
    r2 = time_judge(arrive_list,elev_type)
    if(r2):
        return "2"
    r3 = reach_judge(arrive_list)
    if(r3):
        return "3"
    return ""


if __name__ == "__main__":
    pass