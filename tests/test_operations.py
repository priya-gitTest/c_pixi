"""Tests for math operations."""

import pytest
from mathops import add, multiply


def test_add_positive_numbers():
    """Test addition with two positive integers."""
    assert add(5, 3) == 8

def test_add_negative_numbers():
    """Test addition with two negative integers."""
    assert add(-5, -3) == -8

def test_add_floats():
    """Test addition with floating-point numbers."""
    assert add(1.5, 2.5) == 4.0

def test_multiply_positive_numbers():
    """Test multiplication with two positive integers."""
    assert multiply(4, 5) == 20

def test_multiply_negative_numbers():
    """Test multiplication with a positive and a negative integer."""
    assert multiply(3, -2) == -6

def test_multiply_by_zero():
    """Test multiplication by zero."""
    assert multiply(99, 0) == 0