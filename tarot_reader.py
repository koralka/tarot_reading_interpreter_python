# --->>>  IMPORTING  <<<---
import csv
import difflib
import random

# Initialise an empty dictionary to store tarot card data
tarot_cards = {}

# Open and read the CSV file
with open('cards.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Read as a dictionary

    for row in reader:
        card_name = row['name']  
        tarot_cards[card_name] = {
            'Element': row['element'],  
            'Upright': row['meaning_upright'],  # 
            'Reversed': row['meaning_reversed'],  
            'Arcana': row['arcana'],
            'Suit': row['suit']
        }


# --->>>  TAROT SPREADS  <<<---
tarot_spreads = {
    "Celtic Cross": {
        1: "The Present - this card represents what is happening to the querent at the present time. It also reflects the querent’s state of mind and how they may be perceiving the situation.",
        2: "The Challenge - this card represents the immediate challenge or problem facing the querent. This is the one thing that, if resolved, would make life a lot easier. Even if you draw a ‘positive’ card in this position, consider it carefully as it will still represent a challenge.",
        3: "The Past - this card represents the events that have led up to the present situation and may provide some indication of how the challenge came about.",
        4: "The Future - this card represents what is likely to occur within the next few weeks or even months. This is not the final outcome, simply the next step on the journey.",
        5: "Above - this card reflects the querent’s goal, aspiration, or best outcome with regards to the situation. It is what the querent is working towards consciously as they attempt to resolve the issue.",
        6: "Below - this card reflects that which is within the subconscious realm of the querent and delves much deeper into the core foundation of the situation. It symbolizes the underlying feelings and trends associated with the situation and can indicate what is truly driving the querent. This card may bring a surprise message to the querent, particularly if they are not deeply connected to their inner being (watch out for reversed cards here which are likely to indicate that this is an ‘unknown’ to the querent).",
        7: "Advice - the advice card takes into account all that is happening within the querent’s life and presents a recommendation for what approach can be taken to address the current challenges.",
        8: "External Influences - this card highlights the people, energies, or events which will affect the outcome of the question and are beyond the querent's control.",
        9: "Hopes And/Or Fears - this is perhaps one of the most difficult positions to interpret. Keep in mind that hopes and fears are closely intertwined, therefore that which we hope for may also be that which we fear, and so may fail to happen. Sometimes it is useful to draw a second card for clarification after the reading has been laid and to read the two together.",
        10: "Outcome - this card is representative of where the situation is headed and if/how the issue will be resolved. It assumes the outcome based on the querent continuing their current course of action. Of course, if the outcome card is not a desirable outcome, it is within the free will of the querent to make the necessary changes to their situation."
    },
    "Three-Card Spread": {
        1: "Past",
        2: "Present",
        3: "Future"
    },
    "Five-Card Spread": {
        1: "What is happening now?",
        2: "What is blocking you?",
        3: "What is hidden?",
        4: "What action should you take?",
        5: "What is the outcome?"
    }
}


# --->>>  INPUT  <<<---
while True:  # Keeps the program running until the user decides to exit

    # Display spread choices
    print("\n🔮 Choose a tarot spread:")
    print("1 - Celtic Cross")
    print("2 - Three-Card Spread")
    print("3 - Five-Card Spread")

    spread_choice = input("\nEnter the number of your choice: ")  # User types a number

    # Map user input to the correct spread name
    spread_mapping = {
        "1": "Celtic Cross",
        "2": "Three-Card Spread",
        "3": "Five-Card Spread"
    }

    chosen_spread = spread_mapping.get(spread_choice)  # Get the spread name or return None

    if chosen_spread is None:
        print("\n⚠ Invalid choice. Please restart and enter 1, 2, or 3.")
        exit()  # Stops the script if the user entered an invalid choice

    print(f"\n✨ You chose: {chosen_spread} ✨\n")

    # Get the spread positions dynamically
    spread_positions = tarot_spreads[chosen_spread]

    # -->> helper function to find the closest card name <<--
    def find_closest_card(user_input, card_list):
        """Finds the closest matching card name from the tarot deck."""
        matches = difflib.get_close_matches(user_input, card_list, n=1, cutoff=0.4)
        return matches[0] if matches else None

    # Dictionary to store user input
    user_reading = {}

    # Loop through each position and ask for a card
    for position, meaning in spread_positions.items():
        print(f"\n🔹 Position {position}: {meaning}")

        while True:
            user_input = input("Enter the card you drew (or type 'random' to pick a card for you): ").strip()

            if user_input.lower() == "random":
                card_name = random.choice(list(tarot_cards.keys()))  # Pick a random card
                print(f"✨ Randomly selected: {card_name}")
            else:
                card_name = find_closest_card(user_input, tarot_cards.keys())
                if card_name:
                    print(f"✅ Recognized as: {card_name}")

            if card_name:
                user_reading[position] = card_name
                break
            else:
                print("⚠ Card not found. Please check your spelling and try again.")

            print()  # Adds space between questions


    # --->>>  DISPLAY FINAL READING  <<<---
    # ANSI color codes for Git Bash formatting
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"  # Resets color

    # Fancy dividers
    TOP_BORDER = "╔" + "═" * 48 + "╗"
    BOTTOM_BORDER = "╚" + "═" * 48 + "╝"
    DIVIDER = "╟" + "─" * 48 + "╢"

    # Display tarot reading in a structured way
    print(f"\n{YELLOW}{TOP_BORDER}{RESET}")
    print(f"{BOLD}{YELLOW}🔮 YOUR TAROT READING 🔮".center(50) + f"{RESET}")
    print(f"{YELLOW}{BOTTOM_BORDER}{RESET}")

    for position, card in user_reading.items():
        print(f"\n{CYAN}{DIVIDER}{RESET}")  # Divider between cards
        print(f"{BOLD}{CYAN}🔹 Position {position}: {spread_positions[position]}{RESET}\n")
        
        print(f"🃏 {BOLD}Card Drawn:{RESET} {GREEN}{card}{RESET}")
        print(f"📖 {BOLD}Element:{RESET} {MAGENTA}{tarot_cards[card]['Element']}{RESET}")
        print(f"✨ {BOLD}Arcana:{RESET} {MAGENTA}{tarot_cards[card]['Arcana']}{RESET}")
        
        # Only show suit if it exists (Major Arcana doesn't have a suit)
        if tarot_cards[card]['Suit']:
            print(f"🃏 {BOLD}Suit:{RESET} {MAGENTA}{tarot_cards[card]['Suit']}{RESET}")
        
        print(f"🔺 {BOLD}Upright Meaning:{RESET} {BOLD}{tarot_cards[card]['Upright']}{RESET}")
        print(f"🔻 {BOLD}Reversed Meaning:{RESET} {BOLD}{tarot_cards[card]['Reversed']}{RESET}")

        
    print(f"{YELLOW}{BOTTOM_BORDER}{RESET}\n")  # Final border after the reading

    # --->>>  SAVE READING (option)  <<<---
    while True:
        save_choice = input("\nWould you like to save this reading? (yes/no): ").strip().lower()
        if save_choice in ["yes", "no"]:
            break  # Valid input, exit loop
        print("⚠ Invalid choice. Please enter 'yes' or 'no'.")

    if save_choice == "yes":
        with open("tarot_readings.txt", "a", encoding="utf-8") as file:
            file.write("\n🔮 Tarot Reading 🔮\n")
            file.write("=" * 50 + "\n")
            for position, card in user_reading.items():
                file.write(f"\n🔹 Position {position}: {spread_positions[position]}\n")
                file.write(f"🃏 Card Drawn: {card}\n")
                file.write(f"📖 Element: {tarot_cards[card]['Element']}\n")
                file.write(f"✨ Arcana: {tarot_cards[card]['Arcana']}\n")
                if tarot_cards[card]['Suit']:
                    file.write(f"🃏 Suit: {tarot_cards[card]['Suit']}\n")
                file.write(f"🔺 Upright Meaning: {tarot_cards[card]['Upright']}\n")
                file.write(f"🔻 Reversed Meaning: {tarot_cards[card]['Reversed']}\n")
                file.write("=" * 50 + "\n")

        print("\n📜 Your reading has been saved to 'tarot_readings.txt'!\n")


 # --->>>  ASK TO RESTART/EXIT  <<<---
    while True:
        again = input("\nWould you like to do another reading? (yes/no): ").strip().lower()
        if again in ["yes", "no"]:
            break  # Valid input, exit loop
        print("⚠ Invalid choice. Please enter 'yes' or 'no'.")

    if again == "no":
        print("\n🔮 Thank you for using the Tarot Reader! See you next time! ✨\n")
        break  # Exit loop if they don’t want another reading