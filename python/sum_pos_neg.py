
p = 0
n = 0


for i in range(10):
        num = int(input("Enter integer: "))
        if num >= 0:
            p += num
           
        else:
            n += num
           

print("Sum of positive integers: "+(str(p)))
print("Sum of negative integers: "+(str(n)))
