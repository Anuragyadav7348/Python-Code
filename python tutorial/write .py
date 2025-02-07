# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is an example.\n")
    file.write("File I/O in Python is fun!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
