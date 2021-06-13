

print('dhaka is {1} and chittagong is {0}'.format('dhaka', 'chittagong'))

#positional and keyword argumenmts

print('dhaka is {0} and cumilla is {1} and {others}'.format('dhaka', 'cumilla', others='chittagong'))

#format table

table = {'jack': 1010, 'mack': 20202,'sack': 30303}

print('jack:{jack:d}; mack : {mack:d}; sack: {sack:d}'.format(**table))

#string format

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#IMPORT MATH

import math
print('this is:  %.3f' % math.pi,'pi')


