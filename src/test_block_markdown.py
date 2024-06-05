import unittest

from block_markdown import (
  markdown_to_blocks
)

class TestBlockMarkdown(unittest.TestCase):
  def test_markdown_to_blocks(self):
    input = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
    
    expected_result = [
      "This is **bolded** paragraph",
      "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
      "* This is a list\n* with items"
    ]
    
    self.assertEqual(expected_result, markdown_to_blocks(input))
    
if __name__ == "__main__":
  unittest.main()