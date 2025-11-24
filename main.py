
# main.py - SMART TRAVEL & PACKING ASSISTANT
from packing_data import packing_items, weather_items, travel_tips

# 1. User Inputs

print("=== Welcome to Smart Travel & Packing Assistant ===\n")
destination = input("Enter your travel destination: ")
days = int(input("Enter number of days for the trip: "))
weather = input("Enter expected weather (hot/cold/rainy): ").lower()
travel_type = input("Type of travel (leisure/adventure/business): ").lower()

# Optional follow-up questions
swimming = input("Will you be swimming? (yes/no): ").lower()
if swimming == "yes":
    packing_items.setdefault("Extras", []).append("Swimwear")


# 2. Generate Packing List

final_list = packing_items.copy()

# Add weather-specific items
if weather in weather_items:
    final_list.setdefault("Weather Items", []).extend(weather_items[weather])

# Adjust clothes based on trip duration
final_list["Clothes"] = final_list["Clothes"] * ((days // 3) + 1)


# 3. Display Packing List

print(f"\nPacking List for your trip to {destination} ({days} days, {weather} weather):\n")
for category, items in final_list.items():
    print(f"{category}:")
    for item in items:
        print(f" - {item}")
    print()


# 4. Mark Items as Packed

packed_items = []

print("Mark your items as packed (type 'done' when finished):")
while True:
    packed = input("Enter an item you have packed: ")
    if packed.lower() == "done":
        break
    packed_items.append(packed)

# Show packed items
if packed_items:
    print("\nYou have packed:")
    for item in packed_items:
        print(f" - {item}")

# Show remaining items
print("\nRemaining items to pack:")
for category, items in final_list.items():
    for item in items:
        if item not in packed_items:
            print(f" - {item}")


# 5. Travel Tips

if travel_type in travel_tips:
    print("\nTravel Tips for your trip:")
    for tip in travel_tips[travel_type]:
        print(f" - {tip}")

print("\n=== Happy Traveling! Have a Safe Trip! ===")