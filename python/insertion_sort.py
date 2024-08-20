def insertion(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        
        while j >= 0 and array[j] < value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
        
values = []
for i in range(5):
    user_input = int(input(f"Enter integer {i + 1}: "))
    values.append(user_input)
 
insertion(values)
print("Descending order:")
print(values)