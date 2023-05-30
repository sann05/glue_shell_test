import sys
import os
import searchads_api
import pyeloqua

if __name__ == '__main__':
    help('modules')
    print(searchads_api.__name__)
    print(pyeloqua.__name__)
    sys_paths = sys.path
    print(f"os.getcwd()={os.getcwd()}")
    print(f"os.listdir('.')={os.listdir('.')}")

    print(f"sys.path={sys_paths}")
    for p in sys_paths:
        print(f"os.listdir('{p}')={os.listdir(p)}")
    try:
        from mymodule import module

        module.hello()
        print("Found module")
    except ImportError:
        print("Cannot find module")
    try:
        import module

        module.hello()
        print("Found content")
    except ImportError:
        print("Cannot find content")
