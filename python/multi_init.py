def namesplit(name):
    names = name.split()
    initials = ""

    for word in names:
        while word and word[0] == " ":
            word = word[1:]

        while word and word[-1] == " ":
            word = word[:-1]

        if "-" in word:
            symbols = word.split("-")
            for part in symbols:
                initials += part[0].upper() + "-"
        else:
            initials += word[0].upper() + "."

    if initials and initials[-1] == "-":
        initials = initials[:-1]

    return initials

fullname = input("Enter name: ")
output = namesplit(fullname)
print("Initials: " + output)
