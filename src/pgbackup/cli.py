import argparse


KNOWN_DRIVERS = ["s3", "local"]


class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in KNOWN_DRIVERS:
            parser.error(f"Unkown driver . Available drivers: {KNOWN_DRIVERS}")

        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="postgres connection url")
    parser.add_argument(
        "--driver",
        help="storage driver how and where",
        required=True,
        nargs=2,
        action=DriverAction,
    )
    return parser
