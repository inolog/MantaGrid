# test_mantagrid.py
"""
Tests for MantaGrid module.
"""

import unittest
from mantagrid import MantaGrid

class TestMantaGrid(unittest.TestCase):
    """Test cases for MantaGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MantaGrid()
        self.assertIsInstance(instance, MantaGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MantaGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
