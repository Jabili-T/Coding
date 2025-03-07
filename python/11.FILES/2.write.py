# Open file in write mode and take input from user
with open("output.txt", "w") as file:
    text = input("Enter text: ")
    file.write(text)
print("Text written successfully!!!!!")