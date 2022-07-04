#!/usr/bin/env python

import sys
import os
import string
from itertools import product

for i in range(100):
    for combo in product(string.printable, repeat=i):
        print(''.join(combo))
        os.system('touch ' + combo)
