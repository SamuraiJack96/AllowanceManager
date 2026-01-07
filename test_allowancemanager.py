# test_allowancemanager.py
"""
Tests for AllowanceManager module.
"""

import unittest
from allowancemanager import AllowanceManager

class TestAllowanceManager(unittest.TestCase):
    """Test cases for AllowanceManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AllowanceManager()
        self.assertIsInstance(instance, AllowanceManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AllowanceManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
