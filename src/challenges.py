"""
Week 2 — Harbor Rescue Inventory
"""

from __future__ import annotations


def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """Return the first and last items in the list."""
    
    if len(items) == 0:
        return (None, None)

    first_item = items[0]
    last_item = items[-1]

    return (first_item, last_item)


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """Return a portion of the list based on start and size."""

    if size <= 0:
        return []

    if start < 0 or start >= len(items):
        return []

    end = start + size

    return items[start:end]


def first_supply_index(items: list[object], target: object) -> int:
    """Return the first index of the target item."""

    for index, item in enumerate(items):
        if item == target:
            return index

    return -1


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """Return count and first index of the target item."""

    count = 0
    first_index = -1

    for index, item in enumerate(items):
        if item == target:
            count += 1

            if first_index == -1:
                first_index = index

    return (count, first_index)


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """Return a new list with urgent item at the beginning."""

    updated_list = [urgent_item] + items

    return updated_list