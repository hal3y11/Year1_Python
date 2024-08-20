noOfSweets = 40
noOfStudents = 14
remainSweets = noOfSweets % noOfStudents
sweetsForStudents = noOfSweets - remainSweets
sweetsPerStudent = int(sweetsForStudents/noOfStudents)

print("Teacher has "+ str(noOfSweets) +" sweets to be divided among " + str(noOfStudents))
print("After dividing it among the students she kept "+ str(remainSweets)+ " for herself")
print("Each student gets " + str(sweetsPerStudent) +" sweets.")

