import os

file_path = "text.txt"

if os.access(file_path, os.R_OK):
    print("File has read access")
else:
    print("File does NOT have read access")

if os.access(file_path, os.W_OK):
    print("File has write access")
else:
    print("File does NOT have write access")
