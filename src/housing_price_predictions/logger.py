import colorama
import logging

colorama.init()

# Foreground colors
FORES = {
    "black": colorama.Fore.BLACK,
    "blue": colorama.Fore.BLUE,
    "cyan": colorama.Fore.CYAN,
    "green": colorama.Fore.GREEN,
    "magenta": colorama.Fore.MAGENTA,
    "red": colorama.Fore.RED,
    "white": colorama.Fore.WHITE,
    "yellow": colorama.Fore.YELLOW,
}

# Background colors
BACKS = {
    "black": colorama.Back.BLACK,
    "blue": colorama.Back.BLUE,
    "cyan": colorama.Back.CYAN,
    "green": colorama.Back.GREEN,
    "magenta": colorama.Back.MAGENTA,
    "red": colorama.Back.RED,
    "white": colorama.Back.WHITE,
    "yellow": colorama.Back.YELLOW,
}

# Stylizing options
BRIGHTNESS = {
    "bright": colorama.Style.BRIGHT,
    "dim": colorama.Style.DIM,
    "normal": colorama.Style.NORMAL,
}


def color_string(content, color, brightness=BRIGHTNESS["normal"]) -> None:
    return f"{brightness}{color}{content}{colorama.Style.RESET_ALL}"


class LogFormatter(logging.Formatter):
    # Set format
    debug_format = "[%(asctime)s] %(levelname)-7s | %(filename)s:%(lineno)d | %(message)s"
    info_format = "[%(asctime)s] %(levelname)-7s | %(message)s"
    error_format = "[%(asctime)s] %(levelname)-7s | %(message)s"
    FORMATS = {
        logging.DEBUG: color_string(debug_format, FORES["green"], BRIGHTNESS["dim"]),
        logging.INFO: color_string(info_format, FORES["green"]),
        logging.WARNING: color_string(info_format, FORES["yellow"]),
        logging.ERROR: color_string(error_format, FORES["red"]),
        logging.FATAL: color_string(error_format, FORES["red"], BRIGHTNESS["bright"]),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


def instantiate_logger(app_name="", level=logging.DEBUG):
    logger = logging.getLogger(app_name)
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    ch.setFormatter(LogFormatter())

    logger.addHandler(ch)
    return logger


LOG = instantiate_logger("hpp")
