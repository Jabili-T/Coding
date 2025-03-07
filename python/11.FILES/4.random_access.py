#Read a File Stream with Random Access
with open("text.txt", "r") as file:
    file.seek(20) 
    content = file.read(20)  
    print(content)
