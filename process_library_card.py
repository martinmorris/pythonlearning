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
# print "Due dates: " + str(due_dates)

for date in due_dates:
	date_parts = date.split()
	month = date_parts[0]
	day = date_parts[1]
	year = date_parts[2]
	
	#	print "Month: " + month + " / " + "Day: " + day + " / " + "Year: " + year
	
	if year.startswith("'"):
		new_year = "19" + year[1:]
	elif len(year) == 2:
		new_year = "19" + year
	else:
		new_year = year
		
	print "Date: " + day + " " + month + " " + new_year + " - (" + year + ")"