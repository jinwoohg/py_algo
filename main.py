import sys
import func
def print_hi(*args):
    for i in args:
        print(f' {i}\n')

a = func.what(3)
b = a.what_is_it(4)
if __name__ == '__main__':
    print_hi(sys.argv[1:])
    print(b)



