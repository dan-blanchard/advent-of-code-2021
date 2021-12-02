import argparse
import fileinput
from collections import deque
from itertools import islice


def sliding_window(iterable, n):
    """Taken from itertools docs example"""
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def sliding_sum(*, num_list, n):
    return [sum(window) for window in sliding_window(num_list, n)]



def count_increasing(num_list):
    """Count how many numbers in list of numbers are larger than the previous"""
    return sum(
        (y > x for y, x in zip(reversed(num_list), islice(reversed(num_list), 1, None)))
    )


def main():
    parser = argparse.ArgumentParser(
        description="Count increasing measurements in a file with a measurement per line"
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="*",
        help="Files to read. If empty, stdin is used.",
    )
    parser.add_argument(
        "-n",
        "--window",
        type=int,
        default=1,
        help="Number of items to sum when determining if measurements are increasing or not",
    )
    args = parser.parse_args()
    num_list = [int(line.strip()) for line in fileinput.input(args.files)]
    summed_list = sliding_sum(num_list=num_list, n=args.window)
    num_increasing = count_increasing(summed_list)
    print(f"Total increasing: {num_increasing}")


if __name__ == "__main__":
    main()
