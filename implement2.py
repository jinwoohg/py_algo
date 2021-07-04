import sys

def time(hours):
    minutes = [str(i) for i in range(60)]
    seconds = [str(i) for i in range(60)]
    threes = 0
    hours = hours[1]
    for hour in range(int(hours)+1):
        for minute in minutes:
            for second in seconds:
                if ('3' in second) or ('3' in minute) or ('3' in str(hour)):
                    threes+=1

    return threes


if __name__ == '__main__':
    print(time(sys.argv))