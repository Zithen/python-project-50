from gendiff.main_logic.arg_parse import arg_parser
from gendiff.main_logic.generate_diff import generate_diff


def main():
    generate_diff(arg_parser())


if __name__ == '__main__':
    main()
