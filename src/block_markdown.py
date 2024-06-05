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
  