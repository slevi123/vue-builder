import sys
from pathlib import Path

from decoder import Decoder

if __name__ == "__main__":
    absolute_path = False
    file_compile = False
    minimal = ""

    options = [arg for arg in sys.argv if arg[0] == '-']
    for option in options:
        if option == '--help' or option == '-h':
            print(
                """
    Help for vue-builder:
        -fc, --file-compile input:output : compiles file.
        -a, --absolute : handling input and output paths as absolute paths. (Default is relative)
        -min, --minimal : compiled file will be minified. (Default is normal)
        -vis, --visible : a form between minified and normal.
"""
            )
            break

        elif option == "-min" or option == "--minimal":
            minimal = "minified"

        elif option == "-vis" or option == "--visible":
            minimal = "visible"

        elif option == '-a' or option == '--absolute':
            absolute_path = True

        elif option == '-fc' or option == "--file-compile":
            file_compile = True
        else:
            raise Exception("Can not understand instructions. Use --help to get help.")

    if file_compile:
        if absolute_path:
            input_file, output_file = map(lambda x: Path(x), sys.argv[2].split(':'))
        else:
            input_file, output_file = map(lambda x: Path(f"./{x}"), sys.argv[2].split(':'))

        Decoder(input_file, output_file, minimal=minimal).compile_file()
