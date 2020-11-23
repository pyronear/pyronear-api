# (generated with --quick)

from typing import Optional, Pattern, Type, Union

EPOCH: datetime.datetime
MS_WATERSHED: int
StrBytesIntFloat: Type[Union[bytes, float, int, str]]
date: Type[datetime.date]
date_re: Pattern[str]
datetime: Type[datetime.datetime]
datetime_re: Pattern[str]
errors: module
iso8601_duration_re: Pattern[str]
re: module
standard_duration_re: Pattern[str]
time: Type[datetime.time]
time_re: Pattern[str]
timedelta: Type[datetime.timedelta]
timezone: Type[datetime.timezone]

def from_unix_seconds(seconds: float) -> datetime.datetime: ...
def get_numeric(value: Union[bytes, float, str], native_expected_type: str) -> Optional[Union[float, int]]: ...
def parse_date(value: Union[bytes, float, str, datetime.date]) -> datetime.date: ...
def parse_datetime(value: Union[bytes, float, str, datetime.datetime]) -> datetime.datetime: ...
def parse_duration(value: Union[bytes, float, str]) -> datetime.timedelta: ...
def parse_time(value: Union[bytes, float, str, datetime.time]) -> datetime.time: ...
