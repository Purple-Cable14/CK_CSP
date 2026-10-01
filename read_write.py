# CK, Reading and Writing to Files
# Keywords that let you open the file (With open), then parenthesis = function. in parens 1st write file path(how you get to the file), 2nd pick read(r) or write(w). "as file" = name of file in the code. on next line. "read" = gives what is written on the file. "r+" = read and append.
with open("practice.txt", "r+") as file:
    content = file.read()
    content = "Chapter 1:\n" + content + "And Christopher Robin was sitting on his doorstep putting on his big boots."
    file.write(content)
# "w" = write, replaces content, "a" = append = add to the end
with open("practice.txt", "a") as file:
    file.write("\n Winnie the Pooh and the Blustery Day")