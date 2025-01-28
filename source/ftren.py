"""
File Tools Rename
"""


import os
import re
import glob
from argparse import ArgumentParser, Namespace


def make_name(filepath: str, args: Namespace) -> str:
    """
    Makes a new name
    """

    # get just the file/dir name
    path = os.path.basename(filepath)

    # prefix
    if args.prefix:
        path = args.prefix + path

    # postfix
    if args.postfix:
        path = path + args.postfix

    # regex
    if args.regex:
        for match in re.finditer(args.regex, path):
            path = path.replace(match[0], args.dst)

    return path


# parser
_parser = ArgumentParser(prog="ftren", description="File Tools Rename")
_parser.add_argument("src")
_parser.add_argument("-d", "--dest")
_parser.add_argument("-r", "--regex")
_parser.add_argument("-p", "--prefix")
_parser.add_argument("-P", "--postfix")
_args = _parser.parse_args()

if _args.dest is None:
    _args.dest = _args.src


# renaming
if os.path.isdir(_args.src):
    _args.src += "/*"
    for file in glob.glob(_args.src):
        name = make_name(file, _args)
        os.rename(file, os.path.join(os.path.dirname(file), name))
        print(f"Renamed '{os.path.basename(file)}' to '{name}'")
else:
    name = make_name(_args.src, _args)
    os.rename(_args.src, os.path.join(os.path.dirname(_args.src), name))
    print(f"Renamed '{os.path.basename(_args.src)}' to '{name}'")
