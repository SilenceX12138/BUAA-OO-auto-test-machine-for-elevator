def get_req_info(request=""):
    info_list = request.split('-')
    # id, from floor, to floor
    return (int)(info_list[0]), (int)(info_list[2]), (int)(info_list[4])
