from argparse import ArgumentParser
from datetime import datetime
import dateutil.parser
import time


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--parse', action='store_true')
    parser.add_argument('--milliseconds', '-m', action='store_true')
    parser.add_argument('timestamp', type=str, nargs='?', default=None)
    parsed = parser.parse_args()
    return parsed


def parse_command(args):
    timestamp = int(dateutil.parser.parse(args.timestamp).timestamp() if args.timestamp else time.time())
    return {
        'timestamp': timestamp,
        'local': datetime.fromtimestamp(timestamp - time.timezone),
        'utc': datetime.fromtimestamp(timestamp),
    }


def unixtime_command(args):
    unixtime = float(args.timestamp or time.time())
    timestamp = int(unixtime) if not args.milliseconds else unixtime // 1000
    return {
        'timestamp': timestamp,
        'local': datetime.fromtimestamp(timestamp - time.timezone),
        'utc': datetime.fromtimestamp(timestamp),
    }


COMMAND_FROM_PARSE_FLAG = {
    True: parse_command,
    False: unixtime_command,
}


def main():
    try:
        args = get_args()
        command = COMMAND_FROM_PARSE_FLAG[args.parse]
        results = command(args)
        print('Timestamp: {timestamp}'.format(**results))
        print('    Local: {local}'.format(**results))
        print('      UTC: {utc}'.format(**results))
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
