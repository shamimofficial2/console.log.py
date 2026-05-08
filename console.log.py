""" JavaScript's console.log("Hello World!"); in Python """

import sys

class Console:

    @staticmethod
    def log(text: str) -> None:
        sys.stdout.write(f"{text}\n")

console = Console()

if __name__ == "__main__":
    console.log("Hello World!"); # Output: Hello World!
