import shutil
import os
from page_generator import copy_directory, generate_pages_recursive

def main():
  shutil.rmtree("./public")
  os.mkdir("./public")
  copy_directory("./static", "./public")
  
  generate_pages_recursive("content", "template.html", "public")
  
if __name__=="__main__":
  main()