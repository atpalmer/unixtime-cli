from argparse import ArgumentParser
from datetime import datetime
import time


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--milliseconds', '-m', action='store_true')
    parser.add_argument('unixtime', type=float, nargs='?', default=time.time())
    parsed = parser.parse_args()
    return parsed


def main():
    try:
        args = get_args()
        timestamp = int(args.unixtime if not args.milliseconds else args.unixtime / 1000)
        local = datetime.fromtimestamp(timestamp - time.timezone)
        utc = datetime.fromtimestamp(timestamp)
        print(f'Timestamp: {timestamp}')
        print(f'    Local: {local}')
        print(f'      UTC: {utc}')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
