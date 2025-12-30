def write_file(filename ,text):
    FILE = open(filename, "w")
    FILE.write(text)
    FILE.close()

write_file("info.txt", "Aashutosh Chaudhary")





