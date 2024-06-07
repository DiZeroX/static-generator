import shutil
import os
from page_generator import copy_directory, generate_page

def main():
  shutil.rmtree("./public")
  os.mkdir("./public")
  copy_directory("./static", "./public")
  
  generate_page("content/index.md", "template.html", "public/index.html")
  
if __name__=="__main__":
  main()