ft = int(input("Feet: "))
i = int(input("Inches: "))

Tinches = (ft *12)+i
km = Tinches * 0.0254 / 1000
m = Tinches * 0.0254
cm = Tinches * 2.54
mm = Tinches * 25.4

print("Your height in kilometers: {:.2f}\nYour height in meters: {:.2f}\nYour height in centimeters: {:.2f}\nYour height in millimeters: {:.2f}".format(km,m,cm,mm),sep="\n")