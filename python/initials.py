fullname = input(("Enter your first and family name: "))
names = fullname.split()   
 
Initials = ''.join(name[0].upper() for name in names)
 
print("Initials:", Initials)
 