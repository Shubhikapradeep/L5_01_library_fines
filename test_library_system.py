"""Regression tests for library fine calculations and fine rules."""

import pytest

import library_system


def test_negative_overdue_days_have_no_fine():
    assert library_system.calculate_fine(-3) == 0


def test_positive_overdue_days_calculate_fine():
    assert library_system.calculate_fine(5) == 10


def test_supported_fine_rule():
    assert library_system.fine_from_rule("days * 2 + 10", 4) == 18


def test_unsupported_fine_rule_is_rejected():
    with pytest.raises(ValueError):
        library_system.fine_from_rule("__import__('os').system('echo unsafe')", 4)
