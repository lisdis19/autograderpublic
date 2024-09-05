import unittest
import re

class TodoListGraderTest(unittest.TestCase):
    def setUp(self):
        # Load HTML and CSS content from files (assuming they exist in the working directory)
        with open('todo_list.html', 'r') as html_file:
            self.html_content = html_file.read()
        
        with open('todo_list.css', 'r') as css_file:
            self.css_content = css_file.read()

    def test_background_color(self):
        # Check for light gray background color of the page
        self.assertRegex(self.css_content, r'background-color:\s*#f4f4f4;', "Error: Background color of the page should be #f4f4f4 [-1.0]")

    def test_responsive_design(self):
        # Check for responsive design features (e.g., media queries)
        if not re.search(r'@media', self.css_content):
            self.fail("Error: Missing media queries for responsive design [-2.0]")
        if not re.search(r'max-width', self.css_content):
            self.fail("Error: Missing max-width for responsive behavior [-1.0]")
    
    def test_heading_styles(self):
        # Check for correct heading styles
        self.assertRegex(self.css_content, r'h1\s*{[^}]*font-size:\s*2em;', "Error: Main heading font size should be 2em [-0.5]")
        self.assertRegex(self.css_content, r'h2\s*{[^}]*font-size:\s*1\.17em;', "Error: Secondary heading font size should be 1.17em [-0.5]")
        self.assertRegex(self.css_content, r'h1\s*{[^}]*font-weight:\s*bold;', "Error: Main heading should have bold font weight [-0.5]")
        self.assertRegex(self.css_content, r'h2\s*{[^}]*font-weight:\s*bold;', "Error: Secondary heading should have bold font weight [-0.5]")

    def test_button_styles(self):
        # Check button colors and hover states
        button_colors = {
            'add-assign': ['#007bff', '#0056b3'],
            'clear-completed': ['#64d05e', '#4ea649'],
            'reset': ['#c3c3c3', '#8f8f8f']
        }
        for btn_class, colors in button_colors.items():
            background_color = colors[0]
            hover_color = colors[1]
            self.assertRegex(self.css_content, rf'\.{btn_class}\s*{{[^}}]*background-color:\s*{background_color};', f"Error: {btn_class} button should have background color {background_color} [-1.0]")
            self.assertRegex(self.css_content, rf'\.{btn_class}:hover\s*{{[^}}]*background-color:\s*{hover_color};', f"Error: {btn_class} button should have hover color {hover_color} [-1.0]")

    def test_transition_animation(self):
        # Check for transition animation on button hover
        self.assertRegex(self.css_content, r'button\s*{[^}]*transition:\s*background-color\s*0\.3s;', "Error: Buttons should have a transition animation for background-color with duration of 0.3s [-0.5]")

    def test_rounded_corners(self):
        # Check for rounded corners of the list and tasks
        self.assertRegex(self.css_content, r'\.todo-list\s*{[^}]*border-radius:\s*10px;', "Error: The to-do list should have 10px rounded corners [-0.5]")
        self.assertRegex(self.css_content, r'\.task\s*{[^}]*border-radius:\s*5px;', "Error: Each task should have 5px rounded corners [-0.5]")

    def test_box_shadow(self):
        # Check for 10px box shadow around the list
        self.assertRegex(self.css_content, r'\.todo-list\s*{[^}]*box-shadow:\s*10px;', "Error: The to-do list should have a 10px box shadow [-0.5]")

    def test_input_fields(self):
        # Check for presence of text, date, and checkbox input fields
        self.assertIn('<input type="text"', self.html_content, "Error: Text input field is missing [-0.5]")
        self.assertIn('<input type="date"', self.html_content, "Error: Date input field is missing [-0.5]")
        self.assertIn('<input type="checkbox"', self.html_content, "Error: Checkbox input field is missing [-0.5]")

    def test_dropdown_menu(self):
        # Check for the presence of the dropdown menu
        self.assertRegex(self.html_content, r'<select[^>]*>.*?<option[^>]*>.*?</option>', "Error: Dropdown menu with options is missing [-0.5]")

    def test_font_family(self):
        # Check for Arial font family used throughout
        self.assertRegex(self.css_content, r'font-family:\s*Arial;', "Error: Font family should be Arial throughout the page [-1.0]")

    def test_horizontal_centering(self):
        # Check that the to-do list is centered horizontally with 50px spacing above
        self.assertRegex(self.css_content, r'\.todo-list\s*{[^}]*margin:\s*50px\s*auto;', "Error: The to-do list should be centered horizontally with 50px spacing above it [-1.0]")

    def test_task_background_color(self):
        # Check that each task has a background color of #f4f4f4
        self.assertRegex(self.css_content, r'\.task\s*{[^}]*background-color:\s*#f4f4f4;', "Error: Each task should have a background color of #f4f4f4 [-0.5]")

# Example usage: Run with unittest framework in the Gradescope autograder environment
if __name__ == '__main__':
    unittest.main()

