"""
     1. Read the file and store all the lines in list
     2. Reverse the list
     3. Rewrite the list back to the file
     """

with open('test.txt', 'r') as reader:  # indicates file is being opened in read mode
    content = reader.readline()  # [apple, bat, cat,dog,e]
    reversed(content)  # [e, dog, cat, bat, apple]
    with open('test.txt', 'w') as writer:  # indicates file is being opened in write mode
        for line in reversed(content):
            writer.write(line)
