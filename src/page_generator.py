import os
import shutil

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
  