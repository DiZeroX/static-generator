import re

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
  if re.findall(r"```.*```", markdown):
    return block_type_code
  lines = markdown.splitlines()
  quote_counter = 0
  unordered_list_counter = 0
  ordered_list_counter = 0
  for line in lines:
    if re.findall(r"^>", line):
      quote_counter += 1
    elif re.findall(r"[*-] ", line):
      unordered_list_counter += 1
    elif re.findall(f"{ordered_list_counter + 1}. ", line):
      ordered_list_counter += 1
  if len(lines) == quote_counter:
    return block_type_quote
  if len(lines) == unordered_list_counter:
    return block_type_unordered_list
  if len(lines) == ordered_list_counter:
    return block_type_ordered_list
  return block_type_paragraph
  