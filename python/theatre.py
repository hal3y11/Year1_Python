
adult_price = 10.50
child_price = 7.30
concession_price = 8.40
postage_price = 2.34

total_in_party = int(input("Enter the total number in the party: "))
num_adults = int(input("Enter the number of adults: "))
num_concessions = int(input("Enter the number of concessions: "))
collect_in_person = input("Will the tickets be collected in person? (yes or no): ").lower()

num_children = total_in_party - num_adults - num_concessions

total_cost = (num_adults * adult_price) + (num_children * child_price) + (num_concessions * concession_price)

if num_children >= 10:
    num_free_adults = min(num_children // 10, 10)
else:
    num_free_adults = 0

if total_cost > 100:
    total_cost *= 0.9

if collect_in_person != "yes":
    total_cost += postage_price

print(f"Number of adults: {num_adults}")
print(f"Number of children: {num_children}")
print(f"Number of concessions: {num_concessions}")
print(f"Total cost before discounts and postage: £{total_cost:.2f}")

if num_free_adults > 0:
    print(f"Free adult places: {num_free_adults}")

if total_cost > 100:
    total_cost *= 0.9


print(f"Final total cost: £{total_cost:.2f}")


