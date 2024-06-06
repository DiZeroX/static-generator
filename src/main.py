import shutil
import os
from page_generator import copy_directory

def main():
  shutil.rmtree("./public")
  os.mkdir("./public")
  copy_directory("./static", "./public")
  
if __name__=="__main__":
  main()