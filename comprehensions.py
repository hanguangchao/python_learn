# -*- coding:utf-8 -*-

import os
import glob
import time 

def test_os():
    print(os.getcwd())
    os.chdir("/Users/han/ENV")
    print(os.getcwd())
    
    cwdpath='/Users/han/Code/GitPro/learn-python'
    print(os.path.join(cwdpath, 'myfile.py'))
    print(os.path.expanduser('~'))
    
    pathname='/Users/han/Code/GitPro/learn-python/1.py'
    print(os.path.split(pathname))
    
    (dirname, filename) = os.path.split(pathname)
    print dirname, filename
    
    (shortname, extension) = os.path.splitext(filename)
    print shortname, filename
    
    os.chdir('/Users/han/Code/Py')
    print(glob.glob('*.py'))

    metadata = os.stat('1.py')
    print(metadata)
    
    print(time.localtime(metadata.st_mtime))

    print(os.path.realpath('1.py'))


def test_list_comprehend():
    a_list = [1, 2, 3, 4]
    print([elem * 2 for elem in a_list])
    print(a_list)

    a_list = [elem * 2 for elem in a_list]
    print(a_list)
    
    print([os.path.realpath(f) for f in glob.glob('*') ]) 
    print([(os.path.realpath(f) , os.stat(f).st_size ) for f in glob.glob('*') ]) 

def test_dict_comprehend():
    metadata = [(f, os.stat(f)) for f in glob.glob('*')]
    print(metadata[0])
    
    metadata_dict = {f:os.stat(f).st_mtime for f in glob.glob('*')}
    print(metadata_dict)

    metadata_vk = {v:k for k, v in metadata_dict.items()}
    print(metadata_vk)

def test_set_comprehend():
    a_set = set(range(10))
    print(a_set)
    
    b_set = {x ** 2 for x in a_set}
    print(b_set)

    c_set = {x for x in a_set if x % 2 == 0}
    print(c_set)

    d_set = {2 **x for x in range(10) }
    print(d_set)

if __name__ == '__main__':
    test_os()
    test_list_comprehend()
    test_dict_comprehend()
    test_set_comprehend()
