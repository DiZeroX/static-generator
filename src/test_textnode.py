import unittest

from textnode import TextNode


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
    

if __name__ == "__main__":
  unittest.main()
