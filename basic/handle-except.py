# -*- coding:utf-8 -*-

try:
    file = open('notexist.txt', 'rb')
except IOError as e:
    print('An IOError occurred.{}'.format(e.args[-1]))


try:
    file = open('notexist.txt', 'rb')
except IOError as e:
    print('An IOError occurred.{}'.format(e.args[-1]))
except Exception as e:
    raise e


try:
    file = open('notexist.txt', 'rb')
except IOError as e:
    print('An IOError occurred.{}'.format(e.args[-1]))
except Exception as e:
    raise e
finally:
    print('This would be printed wheather or not an exception occurred!')



try:
    file = open('notexist.txt', 'rb')
except IOError as e:
    print('An IOError occurred.{}'.format(e.args[-1]))
except Exception as e:
    raise e
else:
    print('This would only run if not exception occurs, And an error here would NOT be acught.')
finally:
    print('This would be printed in every case.')
