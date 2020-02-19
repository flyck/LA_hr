from argparse import ArgumentParser, FileType
import sys
from hr import users, inventory

def create_parser():
    parser = ArgumentParser("hr",
            description="A generic hr cli tool."
            )
    parser.add_argument("path", 
            help="The path to the json file.")
    parser.add_argument("--export", 
            action="store_true",
            help="Set this flag to export to the specified path instead of importing."
            )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.export:
        inventory.export(args.path)
        return
    else:
        my_inventory = inventory.read(args.path)
        users.sync(my_inventory)