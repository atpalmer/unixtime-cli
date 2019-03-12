from argparse import ArgumentParser
from datetime import datetime
import time


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--milliseconds', '-m', action='store_true')
    parser.add_argument('timestamp', type=float, nargs='?', default=time.time())
    parsed = parser.parse_args()
    return parsed


def unixtime_command(args):
    timestamp = int(args.timestamp) if not args.milliseconds else float(args.timestamp) // 1000
    return {
        'timestamp': timestamp,
        'local': datetime.fromtimestamp(timestamp - time.timezone),
        'utc': datetime.fromtimestamp(timestamp),
    }


def main():
    try:
        args = get_args()
        command = unixtime_command
        results = command(args)
        print('Timestamp: {timestamp}'.format(**results))
        print('    Local: {local}'.format(**results))
        print('      UTC: {utc}'.format(**results))
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
