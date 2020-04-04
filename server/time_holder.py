import os

import numpy as npy


class time_holder():
    def __init__(self, dirname):
        self.dirname = dirname
        self.time_list = []
        self.mean = 0
        self.var = 0
        self.std = 0
        self.mvp_cnt = 0

    def get_case_time(self):
        outputdir = "./output/" + self.dirname
        output_files = os.listdir(outputdir)
        for output_file in output_files:
            with open(outputdir + "/" + output_file, 'r') as f_opt:
                last_move = f_opt.readlines()[-1]
                pos = last_move.index(']')
                self.time_list.append((float)(last_move[1:pos]))

    def get_stats(self):
        self.mean = npy.mean(self.time_list)
        self.var = npy.var(self.time_list)
        self.std = npy.std(self.time_list, ddof=1)


if __name__ == "__main__":
    t = time_holder("archer")
    t.get_case_time()
    print(t.time_list)
