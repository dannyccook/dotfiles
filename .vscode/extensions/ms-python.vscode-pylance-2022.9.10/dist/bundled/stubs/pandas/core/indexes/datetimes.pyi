from datetime import tzinfo
from typing import overload

import numpy as np
from pandas import (
    DataFrame,
    Timedelta,
    Timestamp,
)
from pandas.core.indexes.accessors import DatetimeIndexProperties
from pandas.core.indexes.api import Float64Index
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin
from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.core.series import (
    TimedeltaSeries,
    TimestampSeries,
)

from pandas._typing import (
    AnyArrayLike,
    ArrayLike,
    DatetimeLike,
    IntervalClosedType,
    np_ndarray_bool,
)

from pandas.core.dtypes.dtypes import DatetimeTZDtype

from pandas.tseries.offsets import BaseOffset

class DatetimeIndex(DatetimeTimedeltaMixin, DatetimeIndexProperties):
    tz: tzinfo | None
    def __init__(
        self,
        data: ArrayLike | AnyArrayLike | list | tuple,
        freq=...,
        tz=...,
        normalize: bool = ...,
        closed=...,
        ambiguous: str = ...,
        dayfirst: bool = ...,
        yearfirst: bool = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
    ): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __reduce__(self): ...
    @overload
    def __add__(self, other: TimedeltaSeries) -> TimestampSeries: ...
    @overload
    def __add__(self, other: Timedelta | TimedeltaIndex) -> DatetimeIndex: ...
    def union_many(self, others): ...
    # overload needed because Index.to_series() and DatetimeIndex.to_series() have
    # different arguments
    def to_series(self, keep_tz=..., index=..., name=...) -> TimestampSeries: ...  # type: ignore[override]
    def snap(self, freq: str = ...): ...
    def get_value(self, series, key): ...
    def get_loc(self, key, method=..., tolerance=...): ...
    def slice_indexer(self, start=..., end=..., step=..., kind=...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    def is_type_compatible(self, typ) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def insert(self, loc, item): ...
    def indexer_at_time(self, time, asof: bool = ...): ...
    def indexer_between_time(
        self, start_time, end_time, include_start: bool = ..., include_end: bool = ...
    ): ...
    def to_perioddelta(self, freq) -> TimedeltaIndex: ...
    def to_julian_date(self) -> Float64Index: ...
    def isocalendar(self) -> DataFrame: ...
    @property
    def tzinfo(self) -> tzinfo | None: ...
    def __lt__(self, other: Timestamp) -> np_ndarray_bool: ...
    def __le__(self, other: Timestamp) -> np_ndarray_bool: ...
    def __gt__(self, other: Timestamp) -> np_ndarray_bool: ...
    def __ge__(self, other: Timestamp) -> np_ndarray_bool: ...
    @property
    def dtype(self) -> np.dtype | DatetimeTZDtype: ...

def date_range(
    start: str | DatetimeLike | None = ...,
    end: str | DatetimeLike | None = ...,
    periods: int | None = ...,
    freq: str | BaseOffset = ...,
    tz: str | tzinfo = ...,
    normalize: bool = ...,
    name: str | None = ...,
    inclusive: IntervalClosedType = ...,
    **kwargs,
) -> DatetimeIndex: ...
def bdate_range(
    start: str | DatetimeLike | None = ...,
    end: str | DatetimeLike | None = ...,
    periods: int | None = ...,
    freq: str | BaseOffset = ...,
    tz: str | tzinfo = ...,
    normalize: bool = ...,
    name: str | None = ...,
    weekmask: str | None = ...,
    holidays: list | None = ...,
    inclusive: IntervalClosedType = ...,
    **kwargs,
) -> DatetimeIndex: ...
