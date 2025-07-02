import logging

from rich.console import Console
from rich.logging import RichHandler


def init_logger(name: str = ""):
    if name == "":
        name = __name__

    logger = logging.getLogger(name)
    logger.propagate = False

    # Create a Rich console
    console = Console()

    # Create RichHandler with custom formatting
    rich_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        show_path=True,
        show_time=True,
        show_level=True,
    )

    # Set the format for log messages
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d (%(funcName)s)): %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    rich_handler.setFormatter(formatter)
    logger.addHandler(rich_handler)

    return logger
