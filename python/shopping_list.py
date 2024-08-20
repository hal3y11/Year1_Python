def get_item_prices():
    items = ["Butter", "Coffee", "Milk", "Kitchen Towel", "Washing Powder"]
    items_prices = []

    for item in items:
        price = float(input(f"Enter the price for {item}: £"))
        items_prices.append((item, price))

    return items_prices

def display_sorted_items(items_prices):
    sorted_items_prices = sorted(items_prices, key=lambda x: x[1], reverse=True)

    print("\nSorted Items and Prices (Highest to Lowest):")
    for item, price in sorted_items_prices:
        print(f"{item}: £{price:.2f}")


print("Enter prices for the following items:")
user_input = get_item_prices()
display_sorted_items(user_input)
