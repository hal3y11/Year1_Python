def user_rating():
    while True:
        try:
            rating = int(input("Please enter a rating (1-5, or -1 to end): "))
            if rating == -1 or (1 <= rating <= 5):
                return rating
            else:
                print("Error: Please enter a valid rating between 1 and 5 or -1 to end.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

ratings_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
total_ratings = 0

while True:
    rating = user_rating()
    if rating == -1:
        break
    ratings_count[rating] += 1
    total_ratings += rating

print("\nRating Summary:")
print("Rating | Count")
for i in range(1, 6):
    print(f"   {i}   |   {ratings_count[i]}")

if total_ratings > 0:
    average_rating = total_ratings / sum(ratings_count.values())
    print(f"\nAverage Rating: {average_rating:.2f}")


