#!/usr/bin/env python

import sys

find = sys.argv[1]
replace = sys.argv[2]
file = open(sys.argv[3], 'r')

text = file.read()

text = text.replace(find, replace)

file.close()

file = open(sys.argv[3], 'w')

file.write(text)

file.close()
