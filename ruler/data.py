with open("input.txt", 'r') as f_in:
    reqs = f_in.readlines()
    for req in reqs:
        if(req[-1] == '\n'):
            print(req, end='')
        else:
            print(req)
