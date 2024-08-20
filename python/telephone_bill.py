min = int(input("Please enter the number of minutes:"))

rate = min * 0.15
vat = rate / 100 * 20
total = rate + vat

print("Number of minutes used: {}\nBasic call charge: £{:.2f}\nVAT due: £{:.2f}\nTotal Bill: £{:.2f}".format(min, rate, vat, total), sep="\n")
