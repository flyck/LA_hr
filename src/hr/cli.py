from argparse import ArgumentParser, FileType
import sys

class ArgumentParser(ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise SystemError(f'Exiting because of an error: {message}')
        sys.exit(1)

def create_parser():
    parser = ArgumentParser("hr",
            description="A generic hr cli tool."
            )
    parser.add_argument("path", 
            nargs=1,
            help="The path to the json file.",
            type=FileType('r', encoding='UTF-8'))
    parser.add_argument("--export", 
            action="store_true", 
            default=False,
            help="Set this flag to export to the specified path instead of importing."
            )

    return parser