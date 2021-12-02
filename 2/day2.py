"""
This solution is just a simplified version of 2020's day 12,
which is why it is probably a little extra verbose
"""

import argparse

import numpy as np


# x, y, degrees
COMMANDS_TO_TRANSFORMS = {
    "forward": (1, 0),
    "up": (0, -1),
    "down": (0, 1),
}


def apply_transform(position, transform, val):
    position = np.add(position, np.multiply(transform, (val, val)))
    return position


def apply_command(position, command, aim):
    command, val = command[0], int(command[1])
    if aim is not None:
        if command == "forward":
            position = apply_transform(position, aim, val)
        else:
            aim = apply_transform(aim, COMMANDS_TO_TRANSFORMS[command], val)
            aim[0] = 1
    else:
        position = apply_transform(position, COMMANDS_TO_TRANSFORMS[command], val)

    return position, aim


def run_program(program, verbose, aim):
    position = np.array((0, 0))
    if verbose:
        print("Submarine at ", end="")
        print_position(position, aim)

    for command in program:
        position, aim = apply_command(position, command, aim)
        if verbose:
            print(f"After command {command}: submarine at ", end="")
            print_position(position, aim)
    return position


def print_position(position, aim):
    x, y = position
    print(f"Horizonal: {x} Depth: {y}" + (f" Aim: {aim[1]}" if aim is not None else ""))


def main():
    parser = argparse.ArgumentParser(
        description="Move submarine following commands",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input_file", help="File with program",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print some debugging output"
    )
    args = parser.parse_args()
    with open(args.input_file) as f:
        program = [line.strip().split() for line in f]
    print(f"Number of lines in file: {len(program)}")
    position = run_program(program, args.verbose, None)
    print(f"Part 1 product of horizontal * depth: {position[0] * position[1]}")
    position = run_program(program, args.verbose, np.array((1, 0)))
    print(f"Part 2 product of horizontal * depth: {position[0] * position[1]}")


if __name__ == "__main__":
    main()
