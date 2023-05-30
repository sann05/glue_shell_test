import sys
import searchads_api
import pyeloqua
from mymodule import module


if __name__ == '__main__':
    help('modules')
    print(searchads_api.__name__)
    print(pyeloqua.__name__)
    module.hello()
