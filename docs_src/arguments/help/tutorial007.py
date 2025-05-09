import doctyper


def main(
    name: str = doctyper.Argument(..., help="Who to greet"),
    lastname: str = doctyper.Argument(
        "", help="The last name", rich_help_panel="Secondary Arguments"
    ),
    age: str = doctyper.Argument(
        "", help="The user's age", rich_help_panel="Secondary Arguments"
    ),
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
