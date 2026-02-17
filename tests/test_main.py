import sys
import os
import pytest

# Add parent directory to path so we can import main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import calculate_factorial

def test_factorial_standard():
    assert calculate_factorial(5) == 120, "Failed input: 5! should be 120"
    assert calculate_factorial(3) == 6, "Failed input: 3! should be 6"

def test_factorial_zero():
    assert calculate_factorial(0) == 1, "Failed input: 0! should be 1"

def test_factorial_negative():
    assert calculate_factorial(-5) is None, "Failed input: Negative numbers should return None"

if __name__ == "__main__":
    pytest.main()