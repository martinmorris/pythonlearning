file_handler = open("library-card.txt", "r")
file_contents = file_handler.read()
file_handler.close()

lines = file_contents.split("\n")

call_number = lines[0]
print "Call number: " + call_number

author_name = lines[1]
print "Author: " + author_name

book_title = lines[2]
print "Book title: " + book_title

due_dates = lines[3:]
# print "Due dates: " + str(due_dates)

# make a list of month abbreviations
all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# create a list to save our clean data
clean_data = []

for date in due_dates:
	date_parts = date.split()
	month = date_parts[0]
	day = date_parts[1]
	year = date_parts[2]
	
	#	print "Month: " + month + " / " + "Day: " + day + " / " + "Year: " + year
	
	# first, dealing with years that have ' in front (e.g. '59)
	if year.startswith("'"):
		new_year = "19" + year[1:]

	# next, deal with years that are just two digits (e.g. 60)
	elif len(year) == 2:
		new_year = "19" + year
		
	# finally, assume any other years are formatted OK and just pass them on
	else:
		new_year = year
		
	print "Date: " + day + " " + month + " " + new_year + " - (" + year + ")"
	assert len(new_year) == 4, "ERROR: Year does not have 4 digits"
	
	# convert month names to numbers
	assert month in all_months, "ERROR: Invalid month name"
	month_index = all_months.index(month)
	new_month = month_index + 1
	
	# print "New month: " + str(new_month)
	print "New Date: " + day + "/" + str(new_month) + "/" + new_year + "\n"
	
	# add our cleaned data to the overall cleaned up list
	# clean_data.append([new_year, str(new_month), day])
	cleaned_due_date = new_year + "-" + str(new_month) + "-" + day
	clean_data.append(cleaned_due_date)

print "Congratulations, data successfully processed!"

# print "Clean data:" + str(clean_data)

# now we need to save out our nicely formatted data!
file_handler = open("library-card-clean.txt", "w")

file_handler.write(call_number + "\n")
file_handler.write(author_name + "\n")
file_handler.write(book_title + "\n")

for cleaned_date in clean_data:
	file_handler.write(cleaned_date + "\n")

file_handler.close()

print "All done, good job!"