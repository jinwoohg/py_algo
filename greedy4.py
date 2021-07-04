import sys
import time


def make_one(args):
    N = int(args[1])
    K = int(args[2])
    count = 0

    while N != 1:

        if N % K == 0 :
            N = N // K
            count += 1

        else:
            count += N % K
            N -= N % K



    return count


if __name__ == '__main__':
    start = time.time()
    print(make_one(sys.argv))
    print(time.time()-start)