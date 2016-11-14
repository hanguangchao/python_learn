# -*- coding: utf-8 -*-

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("anothor arg through *argv:", arg)


def greet_me(**kwargs):
    for key, val in kwargs.items():
        print("{0} == {1}".format(key, val))


def test_argv_kwargv(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


if __name__ == "__main__":
    test_var_args('a', 'b', 'c', 'd')
    test_var_args('a', ('b', 'c', 'd'))

    greet_me(name="a")

    kw = {"name": "a", "age": 12}
    greet_me(**kw)

    args = ('aaa', 1, 2)
    test_argv_kwargv(*args)

    kwargs = {"arg1": 1, "arg2": "v2", "arg3" : "v3"}
    test_argv_kwargv(**kwargs)
