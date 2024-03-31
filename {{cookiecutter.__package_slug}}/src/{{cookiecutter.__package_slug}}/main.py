"""Main code file"""
from os import getlogin
from datetime import datetime
from rich import print


def say_hello(name: str = getlogin()) -> str:
    """Example function to say hello. To be deleted.

    Args:
        name (str, optional): Name to use to say hello. Defaults to "Ephel".

    Returns:
        str: Hello message.
    """
    time_stamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    msg = "[cyan]" 
    + " ".join(["\u2139", "Hello", name + ".", time_stamp]) + "[/cyan]"
    print(msg)
    return msg


if __name__ == "__main__":
    say_hello()
