import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files


class TestFiles(unittest.TestCase):
    @weight(0)
    def test_submitted_files(self):
        """Check submitted files for Assignment 1"""
        # List of expected files for Assignment 1
        expected_files = [
            'monopoly_card.html',  # Part 1: Monopoly card HTML file
            'monopoly_card.css',   # Part 1: Monopoly card CSS file
            'todo_list.html',      # Part 2: To-Do List HTML file
            'todo_list.css'        # Part 2: To-Do List CSS file
        ]

        # Check for missing files
        missing_files = check_submitted_files(expected_files)
        for path in missing_files:
            print(f'Missing {path}')

        # Test will fail if any files are missing
        self.assertEqual(len(missing_files), 0, 'Missing some required files!')
        print('All required files submitted!')
