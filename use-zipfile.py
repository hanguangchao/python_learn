# -*- coding: utf-8 -*-

import zipfile

import os

filename = os.path.realpath(os.path.join(os.path.curdir, '0.zip'))
zFile = zipfile.ZipFile(filename, 'r')
zFile.extractall(pwd='111111')

