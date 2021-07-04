import sys
def card_game(args): # N = 행, M = 열
    args.pop(0)
    N = args.pop(0)
    M = args.pop(0)
    rows = []
    matrix = []
    minvals = []
    for num, i in enumerate(args):
        i = int(i)
        if len(rows) < int(N):
            rows.append(i)
            if num == len(args)-1:
                matrix.append(rows)
        else:
            matrix.append(rows)
            rows = [i]

    for row in matrix:
        minvals.append(min(row))

    return max(minvals)




if __name__ == '__main__':
    answer = card_game(sys.argv)
    print(answer)

