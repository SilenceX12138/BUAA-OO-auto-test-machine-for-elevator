import re


def get_req_info(request=""):
    info_list = re.split(r'(\-FROM\-)|(\-TO\-)', request)
    # id, from floor, to floor
    return int(info_list[0]), int(info_list[3]), int(info_list[6])
