from __future__ import annotations

from bisect import insort
from collections.abc import Iterable, Iterator


class MySet:
    def __init__(self, values: Iterable[str] = ()) -> None:
        self._values: list[str] = []
        for value in values:
            self.add(value)

    def __repr__(self) -> str:
        return f"MySet({self._values!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MySet):
            return NotImplemented
        return self._values == other._values

    def __contains__(self, value: object) -> bool:
        return value in self._values

    def __len__(self) -> int:
        return len(self._values)

    def __iter__(self) -> Iterator[str]:
        return iter(self._values)

    def __or__(self, other: MySet) -> MySet:
        return MySet([*self, *other])

    def __and__(self, other: MySet) -> MySet:
        return MySet([value for value in self if value in other])

    def __lt__(self, other: MySet) -> bool:
        return self <= other and self != other

    def __le__(self, other: MySet) -> bool:
        return all(value in other for value in self)

    def add(self, value: str) -> None:
        if value is None or not value:
            raise ValueError
        if value not in self:
            insort(self._values, value)

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_subset(self, other: MySet) -> bool:
        return self <= other

    def is_superset(self, other: MySet) -> bool:
        return self >= other

    def delete(self, value: object) -> None:
        self._values = [val for val in self if val != value]
