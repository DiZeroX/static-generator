import unittest

from textnode import (
  TextNode,
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
  text_type_text,
  text_type_code,
  text_type_bold 
)


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)
    
  def test_eq_url(self):
    node = TextNode("This is a text node", "bold", "https://google.com")
    node2 = TextNode("This is a text node", "bold", "https://google.com")
    self.assertEqual(node, node2)
    
  def test_eq_url_none(self):
    node = TextNode("This is a text node", "bold", None)
    node2 = TextNode("This is a text node", "bold", None)
    self.assertEqual(node, node2)
    
  def test_not_eq(self):
    node = TextNode("This is a text node", "italic")
    node2 = TextNode("This is a text node", "bold")
    self.assertNotEqual(node, node2)
    
  def test_not_eq_content(self):
    node = TextNode("This is a different text node", "italics")
    node2 = TextNode("This is a text node", "italics")
    self.assertNotEqual(node, node2)
    
  def test_repr(self):
    node = TextNode("This is a text node", "text", "https://www.boot.dev")
    self.assertEqual(
        "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
    )
    
  def test_split_nodes_delimiter_code(self):
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    expected_result = [
      TextNode("This is text with a ", text_type_text),
      TextNode("code block", text_type_code),
      TextNode(" word", text_type_text),
    ]
    self.assertEqual(new_nodes, expected_result)
    
  def test_split_nodes_delimiter_bold(self):
    node = TextNode("This is text with a *bold* word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
    expected_result = [
      TextNode("This is text with a ", text_type_text),
      TextNode("bold", text_type_bold),
      TextNode(" word", text_type_text),
    ]
    self.assertEqual(new_nodes, expected_result)
  
  def test_extract_markdown_images(self):
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    result = extract_markdown_images(text)
    expected_result = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
    self.assertEqual(result, expected_result)
    
  def test_extract_markdown_links(self):
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    result = extract_markdown_links(text)
    expected_result = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
    self.assertEqual(result, expected_result)

if __name__ == "__main__":
  unittest.main()
