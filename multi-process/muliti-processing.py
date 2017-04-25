# -*- coding:utf-8 -*-

import multiprocessing

vfile_list = [1, 2, 3, 4]

def rsync_code(vfile):
    print vfile


if __name__ == '__main__':
    p = multiprocessing.Process(target = rsync_code, args = (vfile_list,))
    p.start()
