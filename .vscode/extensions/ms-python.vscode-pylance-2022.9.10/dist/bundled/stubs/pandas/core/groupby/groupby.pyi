from typing import Callable

from pandas.core.base import (
    PandasObject,
    SelectionMixin,
)
from pandas.core.frame import DataFrame
from pandas.core.generic import NDFrame
from pandas.core.groupby import ops
from pandas.core.groupby.indexing import GroupByIndexingMixin
from pandas.core.indexes.api import Index
from pandas.core.series import Series

from pandas._typing import (
    AxisType,
    FrameOrSeriesUnion,
    KeysArgType,
    NDFrameT,
)

class GroupByPlot(PandasObject):
    def __init__(self, groupby) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, name: str): ...

class BaseGroupBy(PandasObject, SelectionMixin[NDFrameT], GroupByIndexingMixin):
    level = ...
    as_index = ...
    keys = ...
    sort = ...
    group_keys = ...
    squeeze = ...
    observed = ...
    mutated = ...
    obj = ...
    axis = ...
    grouper = ...
    exclusions = ...
    def __init__(
        self,
        obj: NDFrame,
        keys: KeysArgType | None = ...,
        axis: int = ...,
        level=...,
        grouper: ops.BaseGrouper | None = ...,
        exclusions=...,
        selection=...,
        as_index: bool = ...,
        sort: bool = ...,
        group_keys: bool = ...,
        squeeze: bool = ...,
        observed: bool = ...,
        mutated: bool = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    @property
    def groups(self) -> dict[str, str]: ...
    @property
    def ngroups(self): ...
    @property
    def indices(self) -> dict[str, Index]: ...
    def pipe(self, func: Callable, *args, **kwargs): ...
    plot = ...
    def get_group(self, name, obj: DataFrame | None = ...) -> DataFrame: ...

class GroupBy(BaseGroupBy[NDFrameT]):
    def count(self) -> FrameOrSeriesUnion: ...
    def mean(self, **kwargs) -> FrameOrSeriesUnion: ...
    def median(self, **kwargs) -> FrameOrSeriesUnion: ...
    def std(self, ddof: int = ...) -> FrameOrSeriesUnion: ...
    def var(self, ddof: int = ...) -> FrameOrSeriesUnion: ...
    def sem(self, ddof: int = ...) -> FrameOrSeriesUnion: ...
    def ohlc(self) -> DataFrame: ...
    def describe(self, **kwargs) -> FrameOrSeriesUnion: ...
    def resample(self, rule, *args, **kwargs): ...
    def rolling(self, *args, **kwargs): ...
    def expanding(self, *args, **kwargs): ...
    def pad(self, limit: int | None = ...): ...
    def ffill(self, limit: int | None = ...) -> FrameOrSeriesUnion: ...
    def backfill(self, limit: int | None = ...) -> FrameOrSeriesUnion: ...
    def bfill(self, limit: int | None = ...) -> FrameOrSeriesUnion: ...
    def nth(
        self, n: int | list[int], dropna: str | None = ...
    ) -> FrameOrSeriesUnion: ...
    def quantile(self, q=..., interpolation: str = ...): ...
    def ngroup(self, ascending: bool = ...) -> Series: ...
    def cumcount(self, ascending: bool = ...) -> Series: ...
    def rank(
        self,
        method: str = ...,
        ascending: bool = ...,
        na_option: str = ...,
        pct: bool = ...,
        axis: int = ...,
    ) -> DataFrame: ...
    def cummax(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def cummin(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def shift(
        self, periods: int = ..., freq=..., axis: AxisType = ..., fill_value=...
    ): ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: str = ...,
        limit=...,
        freq=...,
        axis: AxisType = ...,
    ) -> FrameOrSeriesUnion: ...
    def head(self, n: int = ...) -> FrameOrSeriesUnion: ...
    def tail(self, n: int = ...) -> FrameOrSeriesUnion: ...
    # Surplus methodss from original pylance stubs; should they go away?
    def first(self, **kwargs) -> FrameOrSeriesUnion: ...
    def last(self, **kwargs) -> FrameOrSeriesUnion: ...
    def max(self, **kwargs) -> FrameOrSeriesUnion: ...
    def min(self, **kwargs) -> FrameOrSeriesUnion: ...
    def size(self) -> Series[int]: ...

def get_groupby(
    obj: NDFrame,
    by: KeysArgType | None = ...,
    axis: int = ...,
    level=...,
    grouper: ops.BaseGrouper | None = ...,
    exclusions=...,
    selection=...,
    as_index: bool = ...,
    sort: bool = ...,
    group_keys: bool = ...,
    squeeze: bool = ...,
    observed: bool = ...,
    mutated: bool = ...,
) -> GroupBy: ...
