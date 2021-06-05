# launch for example:
#   python zp.py 40 125 20000

from sys import argv

script_name, first_param, second_param, third_param = argv

print('ZP = ', (int(first_param) * int(second_param)) + int(third_param))
