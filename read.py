# Open a file and read its content
with open("demofile.txt", "r") as f:
  print(f.read())

# Open a file and with character 
with open("demofile.txt", "r") as f:
  print(f.read(5))  # Read the first 5 characters


# Open a file and overwrite its content
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

# To create a new file in Python, use the open() method, with one of the following parameters:

#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists

# Use "a" here so the script can run safely even if myfile.txt already exists.
with open("myfile.txt", "a") as f:
  f.write("Hello! Welcome to my neww.\n")

# Open the file and read the content:
with open("myfile.txt", "r") as f:
  print(f.read())

# when you want to delete a file, you can use the os.remove() method. Before you can use it, you must import the OS module:
# import os
# os.remove("myfile.txt")