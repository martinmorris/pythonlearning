file_handler = open("library-card.txt", "r")
file_contents = file_handler.read()
file_handler.close()

lines = file_contents.split("\n")

call_number = lines[0]
print "Call number: " + call_number

authorname = lines[1]
print "Author: " + authorname

booktitle = lines[2]
print "Book title: " + booktitle

due_dates = lines[3:]
print "Due dates: " + str(due_dates)