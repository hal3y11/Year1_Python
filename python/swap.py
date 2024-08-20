def swap_numbers(nums):
        nums[0], nums[1] = nums[1], nums[0]

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

numbers = [num1, num2]


print("Original list:", numbers)

swap_numbers(numbers)
print("Swapped list:", numbers)

