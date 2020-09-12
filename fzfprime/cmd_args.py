"""
    :author: David Casado Martínez <dcasadomartinez@gmail.com>
"""
import argparse

DESCRIPTION = (
    "Send to fzf prompt the output of a command. And use the fzf result to "
    "create and execute a command."
)


def parse_input_arguments():
    """ Declare the cmd arguments
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-c",
        "--cmd",
        required=True,
        metavar="cmd",
        help="Command will be executed",
    )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        metavar="file.toml",
        help="config file",
    )

    parser.add_argument(
        "-s",
        "--show",
        required=False,
        help="Display the out command. No execute it",
        action="store_true",
        default=False
    )

    return parser.parse_args()


args = parse_input_arguments()
