# code extracted from https://github.com/classner/pymp

from __future__ import print_function

import numpy as np

ex_array = np.zeros((100,), dtype='uint8')
for index in range(0, 100):
    ex_array[index] = 1
    print('Yay! {} done!'.format(index))