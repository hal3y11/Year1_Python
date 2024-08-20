no =int(input("Enter an integer between 1 and 4 (inclusive): "))
if 1 <= no <= 4:
        
        if no == 1:
            print("Thunderbird 1 pilot is Scott Tracy")
        elif no == 2:
            print("Thunderbird 2 pilot is Virgil Tracy")
        elif no == 3:
            print("Thunderbird 3 pilot is Alan Tracy")
        elif no == 4:
            print("Thunderbird 4 pilot is Gordon Tracy")
else:
        print("Not a permitted number")