#!/usr/bin/env python3
import argparse  # https://docs.python.org/3/library/argparse.html


def func():
    pass


def main():
    if args.v:
        print("There is no version for this.")
    func()
    print("Do your magic here")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A python script.')
    parser.add_argument('-v',
                        action='store_true',
                        default=False,
                        help='Print the version of this template')
    args = parser.parse_args()
    main(args)
