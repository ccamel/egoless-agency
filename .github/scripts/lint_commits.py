#!/usr/bin/env python3
import subprocess
import sys


def valid_message(message):
    return message in (b"\xc2\xb6", b"\xe2\x89\x88", b"\xe2\x88\xb7") or (
        message.endswith(b"\n")
        and message[:-1] in (b"\xc2\xb6", b"\xe2\x89\x88", b"\xe2\x88\xb7")
    )


def main(revision):
    commits = subprocess.check_output(["git", "rev-list", revision]).splitlines()
    invalid = False
    for commit in commits:
        raw = subprocess.check_output(["git", "cat-file", "commit", commit])
        message = raw.split(b"\n\n", 1)[1]
        if not valid_message(message):
            print(f"💀 invalid commit message: {commit.decode()}", file=sys.stderr)
            invalid = True
    return int(invalid)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
