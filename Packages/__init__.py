import os
import pathlib

file = os.fspath(pathlib.Path(__file__).parent.parent.joinpath("Requirements.txt"))
os.system(f"pip install -r {file}")