# -*- coding: utf-8 -*- 

import sys, getopt

print "scrpt name", sys.argv[0]
for i in range(1, len(sys.argv)):
    print "params:", i, sys.argv[i]



opts, args = getopt.getopt(sys.argv[1:], "hi:o")
print(opts)
print(args)
input_file=""
output_file=""
for op, value in opts:
    if op == "-i":
        input_file = value
    elif op == "-o":
        output_file = value
    elif op == "-h":
        usage()
        sys.exit()

