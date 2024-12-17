import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from ctf import get_box_name, get_target_ip, scan_ports, protocol_menu

class TestCTFScript(unittest.TestCase):
    
    def test_get_box_name(self):
        """Test get_box_name function to ensure it returns the correct input."""
        with patch('builtins.input', return_value="TestBox"):
            result = get_box_name()
            self.assertEqual(result, "TestBox")

    def test_get_target_ip_valid(self):
        """Test get_target_ip function with valid input."""
        with patch('builtins.input', return_value="192.168.1.1"):
            result = get_target_ip()
            self.assertEqual(result, "192.168.1.1")

    def test_get_target_ip_nonnumber(self):
        """Test get_target_ip function with invalid IP and retries."""
        with patch('builtins.input', side_effect=["invalid_ip", "85438aaa.1aa.1.10", "192.168.1.1"]):
            result = get_target_ip()
            self.assertEqual(result, "192.168.1.1")


if __name__ == "__main__":
    unittest.main()
