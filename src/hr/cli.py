from argparse import ArgumentParser, FileType
import sys

def create_parser():
    parser = ArgumentParser("hr",
            description="A generic hr cli tool."
            )
    parser.add_argument("path", 
            help="The path to the json file.",
            type=FileType('r', encoding='UTF-8'))
    parser.add_argument("--export", 
            action="store_true",
            help="Set this flag to export to the specified path instead of importing."
            )

    return parser

def main():
    parser = create_parser()
    parser.parse_args()