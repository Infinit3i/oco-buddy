import unittest
from unittest.mock import patch
from Protocols.menu import protocol_menu

class TestMenu(unittest.TestCase):
    def test_protocol_menu(self):
        """Test protocol_menu function to check correct protocol handling."""
        target_ip = "192.168.1.1"
        open_ports = ["22", "80"]

        # Correct structure for MENU_OPTIONS
        mock_menu_options = {
            "1": {"name": "http", "ports": ["80", "443"]},
            "2": {"name": "ssh", "ports": ["22"]},
        }

        # Patch the MENU_OPTIONS and display_protocol_menu at the correct location
        with patch('Protocols.menu.MENU_OPTIONS', mock_menu_options):
            with patch('Protocols.menu.display_protocol_menu') as mock_display:
                protocol_menu(target_ip, open_ports)

                # Verify that display_protocol_menu is called with correct arguments
                mock_display.assert_called_once_with(target_ip, open_ports, mock_menu_options)

if __name__ == "__main__":
    unittest.main()