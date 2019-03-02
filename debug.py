"""Debug the build"""


from pelican import main
import sys


def debug_main():
    print('Begin debug')
    main()
    print('End Debug')


if __name__ == '__main__':
    debug_main()
