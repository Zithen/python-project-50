from gendiff.main_logic.arg_parse import arg_parser
from gendiff.main_logic.gener_diff import generate_diff


def main():
    args = arg_parser()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
