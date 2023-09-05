# pylint: disable=missing-module-docstring
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()
print(contents)
