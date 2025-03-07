# Read file from a specific index
with open("text.txt", "r") as file:
    file.seek(5) 
    print("Reading from index 5:", file.read(15))  