#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.argparser import argparser


def main():
    args = argparser()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
