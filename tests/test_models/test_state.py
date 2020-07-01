#!/usr/bin/python3
"""
Test For state
"""
import unittest
from models.state import State


class TestStateMethod(unittest.TestCase):
    """
    test state class
    """
    def test_state(self):
        """
        test state
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)

if __name__ == '__main__':
    unittest.main()
