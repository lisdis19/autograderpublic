import unittest
import re

class MonopolyCardGraderTest(unittest.TestCase):
    def setUp(self):
        # Load HTML and CSS content from files (assuming they exist in the working directory)
        with open('monopoly_card.html', 'r') as html_file:
            self.html_content = html_file.read()
        
        with open('monopoly_card.css', 'r') as css_file:
            self.css_content = css_file.read()

    def test_alignment(self):
        alignment_elements = ['yellow-box', 'title-deed', 'title-marvin', 'rent', 'house-group', 'hotels-group', 'fine-print', 'card']
        for elem in alignment_elements:
            self.assertRegex(self.html_content, f'class=["\']{elem}["\']', f"Error: {elem} alignment issue [-0.5]")
        # Check if card is horizontally centered
        if not re.search(r'text-align:\s*center;', self.css_content):
            self.fail("Error: Card not horizontally centered [-1.0]")

    def test_font_size(self):
        font_sizes = {
            'title-deed': 'font-size: 2em;',
            'title-marvin': 'font-size: 1.5em;',
            'rent': 'font-size: 1em;',
            'house-group': 'font-size: 0.9em;',
            'hotels-group': 'font-size: 0.9em;',
            'fine-print': 'font-size: 0.75em;'
        }
        for elem, size in font_sizes.items():
            self.assertRegex(self.css_content, f'\.{elem}.*?{size}', f"Error: {elem} incorrect font size [-0.5]")

    def test_spacing(self):
        spacing_elements = ['yellow-box', 'title-deed', 'title-marvin', 'rent', 'house-group', 'hotels-group', 'fine-print']
        for elem in spacing_elements:
            self.assertRegex(self.css_content, f'\.{elem}.*?(margin|padding)', f"Error: {elem} spacing issue [-0.5]")

    def test_borders(self):
        # Check borders for yellow box and the card
        border_elements = {'yellow-box': 'border: 2px solid yellow;', 'card': 'border: 2px solid black;'}
        for elem, border in border_elements.items():
            self.assertRegex(self.css_content, f'\.{elem}.*?{border}', f"Error: {elem} incorrect border [-0.5]")
        # Check for missing borders
        if 'border: 2px solid yellow;' not in self.css_content:
            self.fail("Error: Missing border around yellow box [-1.0]")
        if 'border: 2px solid black;' not in self.css_content:
            self.fail("Error: Missing border around card [-1.0]")

    def test_colors(self):
        # Check colors of elements
        color_elements = {'yellow-box': 'background-color: yellow;', 'card': 'background-color: white;'}
        for elem, color in color_elements.items():
            self.assertRegex(self.css_content, f'\.{elem}.*?{color}', f"Error: {elem} color issue [-2.0]")

    def test_padding_margin(self):
        # Check for incorrect padding/margin around card border and yellow box
        if not re.search(r'padding|margin', self.css_content):
            self.fail("Error: Incorrect padding/margin around card border or yellow box [-0.5]")

    def test_static(self):
        # Check if the card is static (not moving or interactive)
        if re.search(r'animation|transform|transition', self.css_content):
            self.fail("Error: Card is not static [-1.0]")

    def test_font_reasonable(self):
        # Check for reasonable font choice, not strict but must be reasonable
        if re.search(r'Comic Sans|Papyrus', self.css_content):
            self.fail("Error: Unreasonable font used [-2.5]")

    def test_spelling_and_text(self):
        # Check for spelling errors, missing text, and overflows
        required_text = ["TITLE DEED", "MARVIN GARDENS", "RENT $24", "With X House", "Hotels", "&copy;"]
        for text in required_text:
            if text not in self.html_content:
                self.fail(f"Error: Missing or incorrect text - {text} [-2.0]")
        if re.search(r'overflow:\s*visible;', self.css_content):
            self.fail("Error: Text overflows from card [-1.0]")

    def test_html_css_format(self):
        # Check that HTML & CSS are used correctly and that no tables or inline CSS are used
        if '<table>' in self.html_content:
            self.fail("Error: Table elements used [-5.0]")
        if re.search(r'style="', self.html_content):
            self.fail("Error: Inline CSS attributes used instead of in the header [-5.0]")
        if re.search(r'<html>|<head>|<body>', self.html_content) is None:
            self.fail("Error: Incorrect HTML syntax [-5.0]")

    def test_card_size(self):
        # Check for appropriate card dimensions and size
        if not re.search(r'width:\s*\d+px;', self.css_content) or not re.search(r'height:\s*\d+px;', self.css_content):
            self.fail("Error: Incorrect card size [-2.0]")
        if not re.search(r'width:\s*\d+px;', self.css_content):
            self.fail("Error: Inappropriate card dimensions [-2.0]")

# Example usage: Run with unittest framework in the Gradescope autograder environment
if __name__ == '__main__':
    unittest.main()
