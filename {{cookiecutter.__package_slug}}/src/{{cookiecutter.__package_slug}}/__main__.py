"""Main code file"""
from os import getlogin
from datetime import datetime
from rich import print


def hello(name: str = getlogin()) -> str:
    """Example function to say hello. To be deleted.

    Args:
        name (str, optional): Name to use to say hello. Default is current user.

    Returns:
        str: Hello message.
    """
    time_stamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    msg = " ".join(["\u2139", "Hello", name, time_stamp])
    msg = "[cyan]" + msg + "[/cyan]"
    print(msg)
    return msg


if __name__ == "__main__":
    hello()
