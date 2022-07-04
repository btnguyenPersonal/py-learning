#!/usr/bin/env python

import sys
import os
import string
from itertools import product

filename = sys.argv[1]

input_file = open(filename, 'r')
match_text = input_file.read()
os.system('cp ' + filename + ' ' + filename + '.bak')
input_file.close()

target_filename = sys.argv[2]
target_file = open(target_filename, 'r')
target_text = target_file.read()
target_file.close()

for i in range(100):
    for combo in product(string.printable, repeat=i):
        input_string = ''.join(combo)
        cmd_file = open('cmd', 'w')
        cmd_file.write('au VimEnter * ' + input_string + '<esc>:wq')
        cmd_file.close()
        os.system('vim -u cmd' + filename)
        file = open(filename, 'r')
        match_text = file.read()
        file.close()
        if match_text == target_text:
            print(input_string)
        os.system('cp ' + filename + '.bak ' + filename)
