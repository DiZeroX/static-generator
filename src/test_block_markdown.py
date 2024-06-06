import unittest

from block_markdown import (
  markdown_to_blocks,
  block_to_block_type,
  markdown_to_html_node,
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
    
  def test_paragraph(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
    )

  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_lists(self):
    md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
    )

  def test_headings(self):
    md = """
# this is an h1

this is paragraph text

## this is an h2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
    )

  def test_blockquote(self):
    md = """
> This is a
> blockquote block

this is paragraph text

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
    )
    
if __name__ == "__main__":
  unittest.main()