"""
Author: Robert Thomas Kohn
Date: November 10, 2026
Description: A module with functions for calculating averages, cleaning lists,
summarizing readings, converting temperatures, and validating ranges.
Code of honesty: I have not copied from any source without proper citation.
"""


def mean(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)


def clean(readings, marker=-999):
    """Return a new list with every value equal to marker removed."""
    cleaned_readings = []
    for value in readings:
        if value != marker:
            cleaned_readings.append(value)
    return cleaned_readings


def summarize(readings):
    """Return count, mean, minimum, and maximum for a list of readings."""
    count = len(readings)
    avg = mean(readings)
    minimum = min(readings)
    maximum = max(readings)
    return count, avg, minimum, maximum


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit and return it."""
    return (celsius * 9 / 5) + 32


def is_valid(reading, low=-90, high=60):
    """Return True if reading is between low and high, inclusive."""
    return low <= reading <= high


def mean_or_none(numbers):
    """Return the average of a list of numbers, or None if the list is empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
