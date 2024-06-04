import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode("p", "test value", props={"href": "https://www.google.com", "target": "_blank"})
    self.assertEqual(
      ' href="https://www.google.com" target="_blank"',
      node.props_to_html()
    )
    
  
  def test_repr(self):
    child_node = HTMLNode("p", "test value")
    node_props = {"href": "https://www.google.com"}
    node = HTMLNode("div", children=[child_node], props=node_props)
    self.assertEqual(
      "\nHTMLNode(Tag: div Value: None Children: [\nHTMLNode(Tag: p Value: test value Children: None Props: None)\n] Props: {'href': 'https://www.google.com'})\n",
      node.__repr__()
    )
    
class TestLeafNode(unittest.TestCase):
  def test_to_html(self):
    node = LeafNode("test value", tag="p", props={"href": "https://www.google.com", "target": "_blank"})
    self.assertEqual(
      '<p href="https://www.google.com" target="_blank">test value</p>',
      node.to_html()
    )
    
  def test_to_html_no_value(self):
    node = LeafNode(None)
    with self.assertRaises(ValueError):
      node.to_html()
  
if __name__ == "__main__":
  unittest.main()