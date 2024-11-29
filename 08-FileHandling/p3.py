file = open("student.txt", "w")

name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

file.write(name)
file.write(", " + university)
file.write(", " + field)