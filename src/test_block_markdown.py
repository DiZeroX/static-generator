import unittest

from block_markdown import (
  markdown_to_blocks,
  block_to_block_type,
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_quote,
  block_type_unordered_list,
  block_type_ordered_list,
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
  
  def test_block_to_block_type_heading(self):
    input = "### Heading Test"
    self.assertEqual(block_type_heading, block_to_block_type(input))
    
  def test_block_to_block_type_code(self):
    input = "```Code Test```"
    self.assertEqual(block_type_code, block_to_block_type(input))
    
  def test_block_to_block_type_quote(self):
    input = ">Test quote\n>quote2"
    self.assertEqual(block_type_quote, block_to_block_type(input))
    
  def test_block_to_block_type_unordered_list(self):
    input = "* item1\n- item2"
    self.assertEqual(block_type_unordered_list, block_to_block_type(input))
    
  def test_block_to_block_type_ordered_list(self):
    input = "1. item1\n2. item2\n3. item3"
    self.assertEqual(block_type_ordered_list, block_to_block_type(input))
    
  def test_block_to_block_type_paragraph(self):
    input = "paragraph test"
    self.assertEqual(block_type_paragraph, block_to_block_type(input))
    
if __name__ == "__main__":
  unittest.main()