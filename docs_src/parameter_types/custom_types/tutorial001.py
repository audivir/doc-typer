import doctyper


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"<CustomClass: value={self.value}>"


def parse_custom_class(value: str):
    return CustomClass(value * 2)


def main(
    custom_arg: CustomClass = doctyper.Argument(parser=parse_custom_class),
    custom_opt: CustomClass = doctyper.Option("Foo", parser=parse_custom_class),
):
    print(f"custom_arg is {custom_arg}")
    print(f"--custom-opt is {custom_opt}")


if __name__ == "__main__":
    doctyper.run(main)
