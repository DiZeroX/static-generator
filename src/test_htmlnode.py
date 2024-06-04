import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

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

class TestParentNode(unittest.TestCase):
  def test_to_html(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(
      "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
      node.to_html()
    )
  
  def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span><b>grandchild</b></span></div>",
    )

  def test_to_html_many_children(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(
      node.to_html(),
      "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
    )

  def test_headings(self):
    node = ParentNode(
      "h2",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(
      node.to_html(),
      "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
    )

    

class TestLeafNode(unittest.TestCase):
  def test_to_html(self):
    node = LeafNode("p", "test value", props={"href": "https://www.google.com", "target": "_blank"})
    self.assertEqual(
      '<p href="https://www.google.com" target="_blank">test value</p>',
      node.to_html()
    )
    
  def test_to_html_no_value(self):
    node = LeafNode("p", None)
    with self.assertRaises(ValueError):
      node.to_html()
  
if __name__ == "__main__":
  unittest.main()