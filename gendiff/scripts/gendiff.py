from gendiff.cli import get_reference
from gendiff.differ import generate_diff


def main():
    args = get_reference()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
