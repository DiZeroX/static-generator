import re

from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
  def __init__(self, text, text_type, url=None) -> None:
    self.text = text
    self.text_type = text_type
    self.url = url
  
  def __eq__(self, value: object) -> bool:
    return (
      self.text == value.text
      and self.text_type == value.text_type
      and self.url == value.url
    )
  
  def __repr__(self) -> str:
    return f"TextNode({self.text}, {self.text_type}, {self.url})"
  
  
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
  if text_node.text_type == text_type_text:
    return LeafNode(None, text_node.text)
  if text_node.text_type == text_type_bold:
    return LeafNode("b", text_node.text)
  if text_node.text_type == text_type_italic:
    return LeafNode("i", text_node.text)
  if text_node.text_type == text_type_code:
    return LeafNode("code", text_node.text)
  if text_node.text_type == text_type_link:
    return LeafNode("a", None, {"href": text_node.url})
  if text_node.text_type == text_type_image:
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
  raise ValueError(f"Invalid text_type: {text_node.text_type}")
  
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type is not text_type_text:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    sections = old_node.text.split(delimiter)
    if len(sections) % 2 == 0:
        raise ValueError("Invalid markdown, formatted section not closed")
    for i in range(len(sections)):
        if sections[i] == "":
            continue
        if i % 2 == 0:
            split_nodes.append(TextNode(sections[i], text_type_text))
        else:
            split_nodes.append(TextNode(sections[i], text_type))
    new_nodes.extend(split_nodes)
  return new_nodes

def extract_markdown_images(text):
  return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
  return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type is not text_type_text:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    images = extract_markdown_images(old_node.text)
    if len(images) > 0:
      image = images[0]
      sections = old_node.text.split(f"![{image[0]}]({image[1]})", 1)
      if sections[0] != "":
        split_nodes.append(TextNode(sections[0], text_type_text))
      split_nodes.append(TextNode(image[0], text_type_image, url=image[1]))
      if sections[1] != "":
        split_nodes.extend(split_nodes_image([TextNode(sections[1], text_type_text)]))
    new_nodes.extend(split_nodes)
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type is not text_type_text:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    links = extract_markdown_links(old_node.text)
    if len(links) > 0:
      link = links[0]
      sections = old_node.text.split(f"[{link[0]}]({link[1]})", 1)
      if sections[0] != "":
        split_nodes.append(TextNode(sections[0], text_type_text))
      split_nodes.append(TextNode(link[0], text_type_link, url=link[1]))
      if sections[1] != "":
        split_nodes.extend(split_nodes_link([TextNode(sections[1], text_type_text)]))
    else:
      split_nodes.append(old_node)
    new_nodes.extend(split_nodes)
  return new_nodes