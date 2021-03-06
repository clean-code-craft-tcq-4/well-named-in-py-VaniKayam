from referenceManual import colorcode_pair
from colorCodePairUnitTest import *

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ['Blue', 'Orange', 'Green', 'Brown', 'Slate']

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

if __name__ == '__main__':
    
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    colorcode_pair(MAJOR_COLORS,MINOR_COLORS)
    print('Done :)')
