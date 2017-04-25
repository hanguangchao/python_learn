# -*- coding:utf-8 -*-
"""
“上下文管理器允许你在有需要的时候，精确地分配和释放资源。”
"""

class File(object):
    """Context managers 基于类的实现"""
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        # print("Exception has been handled")
        # 处理异常
        # print type, value, traceback
        self.file_obj.close()
        return True

"""基于生成器的实现"""

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'a')
    yield f
    f.close()

if __name__ == '__main__':
    with File('out.log', 'a') as opened_file:
        opened_file.write('AAAAA!\n')

    """
    type, value, traceback:
        <type 'exceptions.AttributeError'> 'file' object has no attribute 'undefined_function' <traceback object at 0x10390a2d8>
    """
    with File('out.log', 'a') as opened_file:
        opened_file.undefined_function('hhhh\n')
    
    with open_file('out.log') as f:
        f.write('Hello\n')

