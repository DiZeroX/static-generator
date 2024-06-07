import os
import shutil
from block_markdown import markdown_to_html_node

def copy_directory(static_path, public_path):
  if not os.path.exists(static_path):
    raise NotADirectoryError(f"Static path '{static_path}' does not exist")
  if not os.path.exists(public_path):
    raise NotADirectoryError(f"Public path '{public_path}' does not exist")
  directories = os.listdir(static_path)
  for directory in directories:
    full_static_path = os.path.join(static_path, directory)
    full_public_path = os.path.join(public_path, directory)
    if os.path.isfile(full_static_path):
      print(f"Copied to: {full_static_path}")
      shutil.copy(full_static_path, full_public_path)
    else:
      os.mkdir(full_public_path)
      copy_directory(full_static_path, full_public_path)

def extract_title(markdown):
  for line in markdown.splitlines():
    if line.startswith("# "):
      return line[2:]
  raise Exception("no h1 header")

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  markdown_file = open(from_path)
  markdown_text = markdown_file.read()
  markdown_file.close()
  template_file = open(template_path)
  template_text = template_file.read()
  template_file.close()
  
  html_text = markdown_to_html_node(markdown_text).to_html()
  title = extract_title(markdown_text)
  edited_template_text = template_text.replace(r"{{ Title }}", title)
  edited_template_text = edited_template_text.replace(r"{{ Content }}", html_text)
  
  dest_path_split = dest_path.split(r"/")
  dest_dirs = "/".join(dest_path_split[0:-1])
  os.makedirs(dest_dirs, exist_ok=True)
  page_html_file = open(dest_path, "w")
  page_html_file.write(edited_template_text)
  page_html_file.close()
  
  
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  content_dirs = os.listdir(dir_path_content)
  for content_dir in content_dirs:
    content_full_path = os.path.join(dir_path_content, content_dir)
    
    if os.path.isfile(content_full_path):
      dest_dir = os.path.splitext(content_dir)[0] + ".html"
      dest_full_path = os.path.join(dest_dir_path, dest_dir)
      generate_page(content_full_path, template_path, dest_full_path)
    else:
      dest_full_path = os.path.join(dest_dir_path, content_dir)
      os.mkdir(dest_full_path)
      generate_pages_recursive(content_full_path, template_path, dest_full_path)