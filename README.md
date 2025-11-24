🧳 Travel & Packing Assistant

A simple Python-based assistant that helps users plan their trip, create a personalized packing list, and track which items they have packed.
It generates items based on destination, weather, trip duration, and travel type, and then lets the user tick off packed items interactively.


---

✨ Features

✔ Accepts user inputs:

Travel destination

Number of days

Weather conditions

Travel type (leisure, business, adventure)

Optional swimming requirement


✔ Automatically generates:

Clothing list

Toiletries

Gadgets

Documents

Weather-specific items

Extra destination-specific recommendations


✔ Allows interactive packing:

User enters items they have packed

Program shows remaining items


✔ Final summary includes:

Packed items

Items still remaining

Travel tips based on travel style



---

📁 Project Structure

travel_packing/
│
├── main.py          # Main program file
├── packing_data.py  # Contains packing lists and helper functions
└── README.md        # Documentation


---

🛠 How It Works

1. User Inputs

The program asks the user:

Destination

Number of days

Weather type (hot/cold/rainy)

Travel type (adventure/business/leisure)

Swimming or not


2. Auto-Generated Packing List

Based on inputs, it creates a personalized packing list using:

Basic lists (clothes, toiletries, etc.)

Weather-based list (hot/cold/rainy)

Travel-type-based list

Optional items like swimwear


3. Interactive Packing

User enters items they have packed:

Enter an item you packed: Jacket
Enter an item you packed: Shoes
Enter an item you packed: done

4. Final Summary

Items packed

Items remaining

Travel tips



---

▶ How to Run the Project
1. Make sure Python is installed.


2. Place both files (main.py and packing_data.py) in the same folder.


3. Open terminal/cmd and run:



python main.py

4. Follow the on-screen instructions.




---

🧩 Example Output

=== Welcome to Smart Travel & Packing Assistant ===

Enter your travel destination: Shimla
Enter number of days: 5
Weather (hot/cold/rainy): cold
Travel type (leisure/adventure/business): leisure
Will you be swimming? (yes/no): no

Generated Packing List for Shimla

Mark items as packed (type 'done' when finished):
Enter item you packed: Jacket
Enter item you packed: done

Packed Items:
 - Jacket

Remaining Items:
 - Socks
 - Tshirts
 - Charger
 - …

=== Happy Traveling! Have a Safe Trip ===


---

🎯 Learning Objectives

This project helps understand:

Python functions

Dictionaries & lists

Modular programming (using multiple files)

User-input handling

Condition-based logic

Interactive console applications

#🏁 Conclusion

The Travel & Packing Assistant is a simple yet effective tool that helps travelers stay organized before a trip.
By generating a personalized packing list based on destination, weather, trip duration, and travel style, it ensures that users do not forget essential items.
Its interactive feature for marking packed items provides clarity, reduces last-minute confusion, and makes the overall packing experience smoother.
This project demonstrates practical use of Python, modular coding, and user-friendly design—making it a valuable beginner-friendly project with real-life application.


---

#👩‍💻 Author

Aditi Sharma
Bioengineering 
VIT Bhopal University
(2025–2029)
