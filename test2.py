#!/usr/bin/python3

from pathlib import Path

tar_files = sorted(Path('./versions').iterdir())
print(tar_files[0])
