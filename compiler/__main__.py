import sys
from pathlib import Path

from compiler.decoder import Decoder


def main():
    helping = False
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
        use -h or --help to display this cheatsheet!
"""
            )
            helping = True
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

    if not helping:
        if file_compile:
            if absolute_path:
                input_file, output_file = map(lambda x: Path(x), sys.argv[2].split(':'))
            else:
                input_file, output_file = map(lambda x: Path(f"./{x}"), sys.argv[2].split(':'))

            Decoder(input_file, output_file, minimal=minimal).compile_file()


if __name__ == "__main__":
    main()
