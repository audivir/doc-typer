import doctyper
from typing_extensions import Annotated


def main(
    name: str,
    lastname: Annotated[
        str, doctyper.Option(help="Last name of person to greet.")
    ] = "",
    formal: Annotated[bool, doctyper.Option(help="Say hi formally.")] = False,
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    doctyper.run(main)
