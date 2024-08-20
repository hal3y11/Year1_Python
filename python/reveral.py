while True:
    Input = input("Enter at least a 2 digits integer or -1 to quit: ")

    if Input == '-1':
        print("Exiting the program.")
        break
  
    if Input.isdigit():
        Input = int(Input)
        
        if 10 <= Input <= 10**10:
            reverse = 0
            ainput = abs(Input) 
            while ainput > 0:
                digit = ainput % 10
                reverse = reverse * 10 + digit
                ainput = ainput // 10

            if Input < 0:
                reverse *= -1

            print("Your reversed integer is: {:02}".format(reverse))
        else:
            print("Invalid input")
    else:
        print("Invalid input")      