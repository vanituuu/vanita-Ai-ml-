# File Handling in Python

File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

# Why do we need File Handling
To store data permanently, even after the program ends.

To access external files like .txt, .csv, .json, etc.

To process large files efficiently without using much memory.

To automate tasks like reading configs or saving outputs.

# Opening a File

To open a file, we can use open() function, which requires file-path and mode as arguments.

**Syntax:**
```py
file = open('filename.txt', 'mode')
```
filename.txt: name (or path) of the file to be opened.

mode: mode in which you want to open the file (read, write, append, etc.).

**Note:** If you don’t specify the mode, Python uses 'r' (read mode) by default.

# Basic Example: Opening a File

 
Explanation: This code opens file Set.txt in read mode. If the file exists, it returns a file object connected to that file; if the file does not exist, Python raises a FileNotFoundErro

# Closing a File
The file.close() method closes the file and releases the system resources. If the file was opened in write or append mode, closing ensures that all changes are properly saved.


# Write operation...
with open("Set.txt","w") as file:      #any file name that you want to write(file in your colab)
  file.write("Helllo, world")

# Read operation...#print are write in it ..
with open("Set.txt","r") as file:  #read tha file
  data= file.read()
  print(data)



