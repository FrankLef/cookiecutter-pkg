"""Main code file"""

from rich import print


def say_hello(name: str = "Ephel") -> str:
    """Example function to say hello. To be deleted.

    Args:
        name (str, optional): Name to use to say hello. Defaults to "Ephel".

    Returns:
        str: Hello message.
    """
    msg = "[cyan]" + " ".join(["\u2139", "Hello", name]) + "[/cyan]"
    print(msg)
    return msg


if __name__ == "__main__":
    say_hello()
