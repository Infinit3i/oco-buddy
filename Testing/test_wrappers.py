import sys
import os
import unittest
from unittest.mock import patch, MagicMock, call

# Ensure Modules directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Import functions from wrappers
from Modules.UI.wrappers import (
    highlight_ports,
    display_background_task,
    header,
    global_command_handler
)

class TestWrappers(unittest.TestCase):
    def test_highlight_ports(self):
        """Test highlight_ports to ensure ports are highlighted correctly."""
        result = highlight_ports(80, [80, 443])
        self.assertIn("\033[32m80\033[0m", result)
        result_no_highlight = highlight_ports(8080, [80, 443])
        self.assertEqual(result_no_highlight, "8080")

    def test_display_background_task(self):
        """Test display_background_task to print tasks correctly."""
        with patch('Modules.All_Pages.wrappers.BACKGROUND_TASK', ["Task1", "Task2"]):
            with patch('builtins.print') as mock_print:
                display_background_task()
                expected_calls = [
                    call("\nBackground Task:"),
                    call("  - Task1"),
                    call("  - Task2")
                ]
                mock_print.assert_has_calls(expected_calls)

    def test_header(self):
        """Test header function for proper output formatting."""
        with patch('builtins.print') as mock_print:
            with patch('Modules.All_Pages.wrappers.clear_screen'):
                with patch('Modules.All_Pages.wrappers.get_random_tip_with_color', return_value="Random Tip"):
                    with patch('Modules.All_Pages.wrappers.center_text', side_effect=lambda x: x):
                        header("192.168.1.1", [80, 443])

                        # Print all calls made to mock_print for debugging
                        print(mock_print.call_args_list)

    def test_global_command_handler_exit(self):
        """Test global_command_handler exits properly on 'exit' command."""
        with patch('builtins.input', side_effect=["exit"]):
            with patch('builtins.print') as mock_print:
                global_command_handler()
                mock_print.assert_any_call("Exiting Command Mode...")

if __name__ == "__main__":
    unittest.main()
