import unittest

from textnode import (
  TextNode,
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
  split_nodes_image,
  split_nodes_link,
  text_to_textnodes,
  text_type_text,
  text_type_code,
  text_type_bold,
  text_type_italic,
  text_type_image,
  text_type_link,
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
    
  def test_split_nodes_image(self):
    node = TextNode(
      "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
      text_type_text
    )
    new_nodes = split_nodes_image([node])
    expected_result = [
      TextNode("This is text with an ", text_type_text),
      TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and another ", text_type_text),
      TextNode(
        "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
      ),
    ]
    self.assertEqual(new_nodes, expected_result)
    
  def test_split_nodes_link(self):
    node = TextNode(
      "This is text with a [link](https://google.com) and another [second link](https://yahoo.com)",
      text_type_text
    )
    new_nodes = split_nodes_link([node])
    expected_result = [
      TextNode("This is text with a ", text_type_text),
      TextNode("link", text_type_link, "https://google.com"),
      TextNode(" and another ", text_type_text),
      TextNode(
        "second link", text_type_link, "https://yahoo.com"
      ),
    ]
    self.assertEqual(new_nodes, expected_result)
    
  def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

  def test_split_image_single(self):
      node = TextNode(
          "![image](https://www.example.com/image.png)",
          text_type_text,
      )
      new_nodes = split_nodes_image([node])
      self.assertListEqual(
          [
              TextNode("image", text_type_image, "https://www.example.com/image.png"),
          ],
          new_nodes,
      )

  def test_split_images(self):
      node = TextNode(
          "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
          text_type_text,
      )
      new_nodes = split_nodes_image([node])
      self.assertListEqual(
          [
              TextNode("This is text with an ", text_type_text),
              TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
              TextNode(" and another ", text_type_text),
              TextNode(
                  "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
              ),
          ],
          new_nodes,
      )

  def test_split_links(self):
      node = TextNode(
          "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
          text_type_text,
      )
      new_nodes = split_nodes_link([node])
      self.assertListEqual(
          [
              TextNode("This is text with a ", text_type_text),
              TextNode("link", text_type_link, "https://boot.dev"),
              TextNode(" and ", text_type_text),
              TextNode("another link", text_type_link, "https://blog.boot.dev"),
              TextNode(" with text that follows", text_type_text),
          ],
          new_nodes,
      )
  
  def test_text_to_textnodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    expected_result = [
      TextNode("This is ", text_type_text),
      TextNode("text", text_type_bold),
      TextNode(" with an ", text_type_text),
      TextNode("italic", text_type_italic),
      TextNode(" word and a ", text_type_text),
      TextNode("code block", text_type_code),
      TextNode(" and an ", text_type_text),
      TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and a ", text_type_text),
      TextNode("link", text_type_link, "https://boot.dev"),
    ]
    self.assertEqual(expected_result, text_to_textnodes(text))



if __name__ == "__main__":
  unittest.main()
