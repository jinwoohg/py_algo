import sys


def moving_loc(current_loc):
    col_num = ord(current_loc[1][0])-ord('a')+1
    row_num = current_loc[1][1]
    possible_mv = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
    result = 0
    for mv in possible_mv:
        if int(col_num) + mv[0] < 1 or int(col_num) + mv[0] > 7 or int(row_num) + mv[1] < 1 or int(row_num) + mv[1] > 7:
            continue
        else:
            result += 1

    return result


if __name__ == '__main__':
    print(moving_loc(sys.argv))