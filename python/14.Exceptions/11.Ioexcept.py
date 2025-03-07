#IOException
try:
    with open("/root/forbidden_file.txt", "r") as file: 
        content = file.read()
except IOError:
    print("***IO error occurred!")
