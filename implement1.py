import sys

def lrud(args):
    num_of_matrix = int(args[1])
    current_loc = [1,1]
    for mv in args[2:] :
        if mv == 'R':
            if current_loc[1] < num_of_matrix:
                current_loc[1] += 1
            else:
                continue
        elif mv == 'L':
            if current_loc[1] > 1:
                current_loc[1] -= 1
            else:
                continue
        elif mv == 'U':
            if current_loc[0] > 1:
                current_loc[0] -= 1
            else:
                continue
        elif mv == 'D':
            if current_loc[0] < num_of_matrix:
                current_loc[0] += 1
            else:
                continue

    return current_loc

if __name__ == '__main__':
    print(lrud(sys.argv))

