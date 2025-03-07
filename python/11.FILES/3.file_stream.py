# Read a file stream line by line
with open("text.txt", "r") as file:
    for line in file:
        print(line,end=" ")  
