#!/usr/bin/python3
"""
Reads from standard input and computes metrics
"""

if __name__ == "__main__":
    import sys

    stdin = sys.stdin

    count = 0
    total_size = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_counts = {}

    try:
        for line in stdin:
            if count == 10:
                print("File size: {}".format(total_size))
                for code in sorted(status_counts):
                    print("{}: {}".format(code, status_counts[code]))
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_counts.get(line[-2], -1) == -1:
                        status_counts[line[-2]] = 1
                    else:
                        status_counts[line[-2]] += 1
            except IndexError:
                pass

        print("File size: {}".format(total_size))
        for code in sorted(status_counts):
            print("{}: {}".format(code, status_counts[code]))

    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for code in sorted(status_counts):
            print("{}: {}".format(code, status_counts[code]))
        raise
