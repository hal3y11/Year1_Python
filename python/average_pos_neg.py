p = 0
n = 0
p_count = 0
n_count = 0

for i in range(10):
    num = int(input("Enter integer: "))
    if num >= 0:
        p += num
        p_count += 1
    else:
        n += num
        n_count += 1

if p_count > 0:
    avg_positive = p / p_count
    print("Sum of positive integers:", p)
    print("Average of positive integers:", avg_positive)
else:
    print("No positive integers entered.")

if n_count > 0:
    avg_negative = n / n_count
    print("Sum of negative integers:", n)
    print("Average of negative integers:", avg_negative)
else:
    print("No negative integers entered.")
