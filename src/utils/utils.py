from os import environ
from datetime import datetime, timezone, timedelta


def get_datetime(
    offset_hour: int = 0, offset_minute: int = 0, offset_second: int = 0
) -> datetime:
    """Get the current datetime according to a TIMEZONE specified as an
    environment variable.
    :param offset_hour: int - Number of hours to add to date
    :param offset_minute: int - Number of minutes to add to date
    :param offset_second: int - Number of seconds to add to date
    :return datetime - Date with offset
    """
    timezone_offset = int(-6)
    tzinfo = timezone(timedelta(hours=timezone_offset))
    return datetime.now(tzinfo)


def logger(message: str):
    print(get_datetime(), " " + message)
