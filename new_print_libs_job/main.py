import sys
from inner_module import inner_file
import searchads_api
import pyeloqua
import local_file

if __name__ == '__main__':
    help('modules')
    print(inner_file.NAME)
    print(local_file.NAME)
    print(searchads_api.__name__)
    print(pyeloqua.__name__)
