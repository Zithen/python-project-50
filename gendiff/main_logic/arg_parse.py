import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.') # noqa E501
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()
