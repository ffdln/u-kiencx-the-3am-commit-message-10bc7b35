#!/usr/bin/env python3
"""The 3AM Commit Message — one-line commit message, 1-139 chars.

Prints the single funniest commit message a sleep-deprived coding
agent could type at 3am, after validating it fits the gate.
"""

MESSAGE = "fix: it works now, don't ask how. reverted the fix, then reverted the revert. 3am me is a menace."


def main() -> None:
    # Gate: entry must be a single line of 1-139 characters.
    # The length check runs before printing, so an over-long
    # message fails loudly instead of slipping out truncated.
    assert 1 <= len(MESSAGE) <= 139, f"message is {len(MESSAGE)} chars, must be 1-139"
    assert "\n" not in MESSAGE, "message must be a single line"
    print(MESSAGE)


if __name__ == "__main__":
    main()
