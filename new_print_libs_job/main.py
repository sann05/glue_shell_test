import sys
from inner_module import inner_file
import local_file

if __name__ == '__main__':
    help('modules')
    print(inner_file.NAME)
    print(local_file.NAME)
