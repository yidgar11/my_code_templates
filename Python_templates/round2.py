__author__ = 'yidgar'

#Make a function `round` that rounds a number to closest integer.

import sys
import os.path

number = sys.argv[1]

def round_num(num, step=1):
    div, mod = divmod(num, step)
    if mod <= (step/2):
        return div * step
    else:
        return div * step  + step



print(round_num(float(number)))

# x = 7.6
#
# x % 1 --> 0.6
#
# x // 1 --> 7.0
