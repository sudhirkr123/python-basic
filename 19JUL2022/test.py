#read the file
reading_file = open("d:\\sample.txt", "r")
new_file_content = ""
for line in reading_file:
    stripped_line = line.strip()
    new_line = stripped_line.replace("india", "nd")
    new_file_content += new_line +"\n"
reading_file.close()

writing_file = open("d:\\sample.txt", "w")
writing_file.write(new_file_content)
writing_file.close()
