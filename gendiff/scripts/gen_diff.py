from gendiff.main_logic.arg_parser import parse_arguments
from gendiff.main_logic.diff_generator import generate_diff


def main():
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
