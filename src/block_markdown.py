import re
from htmlnode import ParentNode, LeafNode
from textnode import text_to_textnodes, text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
  blocks = []
  temp_block = ""
  lines = markdown.splitlines()
  for line in lines:
    if line == "":
      if temp_block:
        blocks.append(temp_block.strip())
        temp_block = ""
      continue
    temp_block += f"{line}\n"
  if temp_block:
    blocks.append(temp_block.strip())
  return blocks

def block_to_block_type(markdown):
  if re.findall(r"^#{1,6} ", markdown):
    return block_type_heading
  if re.findall(r"^```.*```", markdown):
    return block_type_code
  lines = markdown.splitlines()
  quote_counter = 0
  unordered_list_counter = 0
  ordered_list_counter = 0
  for line in lines:
    if re.findall(r"^>", line):
      quote_counter += 1
    elif re.findall(r"^[*-] ", line):
      unordered_list_counter += 1
    elif re.findall(f"^{ordered_list_counter + 1}. ", line):
      ordered_list_counter += 1
  if len(lines) == quote_counter:
    return block_type_quote
  if len(lines) == unordered_list_counter:
    return block_type_unordered_list
  if len(lines) == ordered_list_counter:
    return block_type_ordered_list
  return block_type_paragraph

def text_to_children(markdown):
  inline_text_nodes = text_to_textnodes(markdown)
  children_nodes = []
  for text_node in inline_text_nodes:
    html_node = text_node_to_html_node(text_node)
    children_nodes.append(html_node)
  return children_nodes

def paragraph_to_html_node(markdown):
  lines = markdown.splitlines()
  paragraph_text = " ".join(lines)
  children_nodes = text_to_children(paragraph_text)
  return ParentNode("p", children_nodes)

def heading_to_html_node(markdown):
  hashtag_counter = 0
  for character in markdown:
    if character != "#":
      break
    hashtag_counter += 1
  text = markdown[hashtag_counter+1:]
  children_nodes = text_to_children(text)
  return ParentNode(f"h{hashtag_counter}", children_nodes)

def code_to_html_node(markdown):
  text = markdown.strip("```")
  children_nodes = text_to_children(text)
  code_node = ParentNode("code", children_nodes)
  return ParentNode("pre", [code_node])

def quote_to_html_node(markdown):
  new_lines = []
  for line in markdown.splitlines():
    if line.startswith(">"):
      new_lines.append(line[1:].strip())
  removed_quote_markdown = " ".join(new_lines)
  children_nodes = text_to_children(removed_quote_markdown)
  return ParentNode("blockquote", children_nodes)

def unordered_list_to_html_node(markdown):
  children_nodes = []
  for line in markdown.splitlines():
    text = line[2:]
    inline_nodes = text_to_children(text)
    child_node = ParentNode("li", inline_nodes)
    children_nodes.append(child_node)
  return ParentNode("ul", children_nodes)

def ordered_list_to_html_node(markdown):
  children_nodes = []
  for line in markdown.splitlines():
    number_position = line.find(". ") + 2
    text = line[number_position:]
    inline_nodes = text_to_children(text)
    child_node = ParentNode("li", inline_nodes)
    children_nodes.append(child_node)
  return ParentNode("ol", children_nodes)

def markdown_to_html_node(markdown):
  block_children = []
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    html_node = None
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
      html_node = paragraph_to_html_node(block)
    elif block_type == block_type_heading:
      html_node = heading_to_html_node(block)
    elif block_type == block_type_code:
      html_node = code_to_html_node(block)
    elif block_type == block_type_quote:
      html_node = quote_to_html_node(block)
    elif block_type == block_type_unordered_list:
      html_node = unordered_list_to_html_node(block)
    elif block_type == block_type_ordered_list:
      html_node = ordered_list_to_html_node(block)
    else:
      raise ValueError("Invalid block")
    block_children.append(html_node)
  return ParentNode("div", block_children)