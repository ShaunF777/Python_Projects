#!/usr/bin/env python3
"""
🐍 Interactive Python Learning Program 🐍
========================================

This program interactively teaches Python programming concepts including:
- While loops and for loops
- Lists and list operations
- Dictionaries and data structures
- User input validation
- String manipulation and formatting
- Basic programming patterns and best practices

Uses beloved characters from:
- Peter Rabbit books by Beatrix Potter
- The Famous Five series by Enid Blyton  
- The Faraway Tree books by Enid Blyton

Dependencies:
- Python 3.6+ (uses f-strings)
- No external libraries required - uses only built-in Python modules
"""

import random
import time
import sys

# Character data for our examples
PETER_RABBIT_CHARACTERS = ["Peter", "Flopsy", "Mopsy", "Cotton-tail", "Benjamin"]
FAMOUS_FIVE_CHARACTERS = ["Julian", "Dick", "Anne", "George", "Timmy"]
FARAWAY_TREE_CHARACTERS = ["Jo", "Bessie", "Fanny", "Rick", "Silky", "Moonface", "Saucepan Man", "Dame Washalot", "The Angry Pixie"]

def clear_screen():
    """Clear the screen for better presentation"""
    print("\n" * 5)

def type_effect(text, delay=0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_name():
    """Get the user's name with validation"""
    while True:
        print("🌟 Welcome to the Interactive Python Learning Adventure! 🌟")
        name = input("\n😊 What's your name, fellow programmer? ").strip()
        if name:
            return name
        print("🤔 I didn't catch that! Please tell me your name.")

def press_enter_to_continue():
    """Wait for user to press enter"""
    input("\n📚 Press Enter to continue your learning journey...")

def demonstrate_basic_loops(name):
    """Teach basic loop concepts"""
    clear_screen()
    print(f"🐰 Chapter 1: Learning Loops with Peter Rabbit! 🐰")
    print("=" * 50)
    
    type_effect(f"\nHello {name}! Let's start with Peter Rabbit in Mr. McGregor's garden...")
    
    # Bad way - repetitive code
    print("\n❌ First, let's see the WRONG way to make Peter hop:")
    print('print("🐰 Peter hops!")')
    print('print("🐰 Peter hops!")')
    print('print("🐰 Peter hops!")')
    
    choice = input(f"\n🤔 {name}, what's wrong with this approach? (type 'repetitive' or 'boring'): ").lower()
    if 'repetitive' in choice or 'boring' in choice:
        print("✅ Exactly! It's repetitive and hard to maintain!")
    else:
        print("💡 It's repetitive and hard to maintain - imagine doing this 100 times!")
    
    press_enter_to_continue()
    
    # While loop demonstration
    clear_screen()
    print("🔄 WHILE LOOPS - The Persistent Approach")
    print("=" * 40)
    
    print("\n💡 A while loop keeps running WHILE a condition is true!")
    print("\nLet's help Peter count his hops:")
    
    print("\n📝 Code Example:")
    print("hops = 0")
    print("while hops < 3:")
    print("    print(f'🐰 Peter hop #{hops + 1}!')")
    print("    hops += 1")
    
    print("\n🎬 Let's see it in action:")
    hops = 0
    while hops < 3:
        print(f"🐰 Peter hop #{hops + 1}!")
        hops += 1
        time.sleep(0.5)
    
    quiz_answer = input(f"\n🧠 Quiz time, {name}! What would happen if we forgot 'hops += 1'? ")
    if 'infinite' in quiz_answer.lower() or 'forever' in quiz_answer.lower():
        print("🎯 Perfect! It would create an infinite loop!")
    else:
        print("💡 It would create an infinite loop - Peter would hop forever!")
    
    press_enter_to_continue()

def demonstrate_for_loops(name):
    """Teach for loops with examples"""
    clear_screen()
    print("🌟 FOR LOOPS - The Elegant Solution")
    print("=" * 35)
    
    print(f"\n{name}, for loops are more elegant when we know how many times to repeat!")
    
    print("\n📝 Simple for loop with range:")
    print("for i in range(3):")
    print("    print(f'🐰 Hop {i + 1}!')")
    
    print("\n🎬 Output:")
    for i in range(3):
        print(f"🐰 Hop {i + 1}!")
        time.sleep(0.3)
    
    print("\n🎯 Pro tip: When we don't use the variable, we use underscore:")
    print("for _ in range(3):")
    print("    print('🐰 Peter hops!')")
    
    user_range = get_positive_integer(f"\n🤔 {name}, how many times should Peter hop? ")
    
    print(f"\n🎪 Peter performs {user_range} hops:")
    for _ in range(user_range):
        print("🐰 Boing!", end=" ")
        time.sleep(0.2)
    print("\n\n🎉 Great job, Peter!")
    
    press_enter_to_continue()

def demonstrate_lists(name):
    """Teach lists with character examples"""
    clear_screen()
    print("📝 LISTS - Organizing Our Characters")
    print("=" * 35)
    
    print(f"\n{name}, let's organize the Famous Five into a list!")
    
    print("\n💡 A list is a collection of items in order:")
    print(f"famous_five = {FAMOUS_FIVE_CHARACTERS}")
    
    print(f"\n🔍 We can access items by their position (starting from 0):")
    for i, character in enumerate(FAMOUS_FIVE_CHARACTERS):
        print(f"famous_five[{i}] = '{character}'")
        time.sleep(0.3)
    
    # Interactive quiz
    quiz_index = random.randint(0, len(FAMOUS_FIVE_CHARACTERS) - 1)
    answer = input(f"\n🧠 Quick quiz! Who is at position {quiz_index}? ")
    
    if answer.lower() == FAMOUS_FIVE_CHARACTERS[quiz_index].lower():
        print("🎯 Brilliant! You're getting the hang of lists!")
    else:
        print(f"💡 Close! It's {FAMOUS_FIVE_CHARACTERS[quiz_index]}. Remember, we start counting from 0!")
    
    # Demonstrate list iteration
    print(f"\n🔄 We can visit each character using a for loop:")
    print("for character in famous_five:")
    print("    print(f'Hello, {character}! 👋')")
    
    print("\n🎬 Let's greet everyone:")
    for character in FAMOUS_FIVE_CHARACTERS:
        print(f"Hello, {character}! 👋")
        time.sleep(0.4)
    
    # Length function
    print(f"\n📏 The len() function tells us how many items are in a list:")
    print(f"len(famous_five) = {len(FAMOUS_FIVE_CHARACTERS)}")
    
    press_enter_to_continue()

def demonstrate_list_operations(name):
    """Demonstrate more advanced list operations"""
    clear_screen()
    print("🔧 ADVANCED LIST OPERATIONS")
    print("=" * 30)
    
    print(f"\n{name}, let's explore more list magic with the Faraway Tree friends!")
    
    # Create a working list
    tree_friends = FARAWAY_TREE_CHARACTERS.copy()
    print(f"🌳 Current tree friends: {tree_friends}")
    
    # Adding items
    new_friend = input(f"\n✨ {name}, let's add a new friend to the tree! What's their name? ")
    tree_friends.append(new_friend)
    print(f"🎉 Added {new_friend}! Now we have: {tree_friends}")
    
    # List with index
    print(f"\n📋 Let's number our friends:")
    for i in range(len(tree_friends)):
        print(f"{i + 1}. {tree_friends[i]}")
        time.sleep(0.2)
    
    # Remove item
    if len(tree_friends) > 1:
        print(f"\n😢 Oh no! Someone has to climb down from the tree...")
        remove_index = random.randint(0, len(tree_friends) - 1)
        removed_friend = tree_friends.pop(remove_index)
        print(f"👋 {removed_friend} climbed down! Remaining friends: {tree_friends}")
    
    press_enter_to_continue()

def demonstrate_dictionaries(name):
    """Teach dictionaries with character data"""
    clear_screen()
    print("📚 DICTIONARIES - Character Profiles")
    print("=" * 35)
    
    print(f"\n{name}, dictionaries let us store more information about our characters!")
    print("💡 Instead of just names, we can store names AND their details!")
    
    # Simple dictionary
    print("\n📝 Simple dictionary example:")
    rabbit_homes = {
        "Peter": "Under the fir tree",
        "Benjamin": "Near the garden wall", 
        "Flopsy": "The burrow",
        "Mopsy": "The burrow",
        "Cotton-tail": "The burrow"
    }
    
    print("rabbit_homes = {")
    for rabbit, home in rabbit_homes.items():
        print(f'    "{rabbit}": "{home}",')
        time.sleep(0.3)
    print("}")
    
    # Accessing dictionary values
    test_rabbit = random.choice(list(rabbit_homes.keys()))
    print(f"\n🔍 To find where {test_rabbit} lives:")
    print(f'rabbit_homes["{test_rabbit}"] = "{rabbit_homes[test_rabbit]}"')
    
    # Interactive quiz
    quiz_rabbit = input(f"\n🏠 {name}, which rabbit would you like to visit? ")
    if quiz_rabbit in rabbit_homes:
        print(f"🎯 Great choice! {quiz_rabbit} lives {rabbit_homes[quiz_rabbit]}!")
    else:
        print(f"🤔 I don't know {quiz_rabbit}. Try: {', '.join(rabbit_homes.keys())}")
    
    press_enter_to_continue()

def demonstrate_complex_dictionaries(name):
    """Show more complex dictionary structures"""
    clear_screen()
    print("🎭 COMPLEX DICTIONARIES - Detailed Profiles")
    print("=" * 40)
    
    print(f"\n{name}, let's create detailed character profiles!")
    
    # List of dictionaries
    characters = [
        {"name": "Peter", "species": "Rabbit", "personality": "Mischievous", "favorite_food": "Carrots"},
        {"name": "Julian", "species": "Human", "personality": "Leader", "favorite_food": "Sandwiches"},
        {"name": "Silky", "species": "Fairy", "personality": "Gentle", "favorite_food": "Dewdrops"},
        {"name": "Moonface", "species": "Moon-man", "personality": "Cheerful", "favorite_food": "Pop cakes"}
    ]
    
    print("📋 Our character database:")
    print("characters = [")
    for char in characters:
        print(f"    {char},")
        time.sleep(0.5)
    print("]")
    
    print(f"\n🔄 Let's meet each character:")
    for character in characters:
        print(f"\n👋 Meet {character['name']}!")
        print(f"   🧬 Species: {character['species']}")
        print(f"   😊 Personality: {character['personality']}")
        print(f"   🍽️ Favorite food: {character['favorite_food']}")
        time.sleep(1)
    
    # Interactive character selection
    print(f"\n🎮 {name}, let's play a character guessing game!")
    chosen_char = random.choice(characters)
    
    print(f"🎭 I'm thinking of a {chosen_char['personality'].lower()} {chosen_char['species'].lower()}...")
    print(f"💭 They love eating {chosen_char['favorite_food'].lower()}...")
    
    guess = input("🤔 Who am I thinking of? ")
    if guess.lower() == chosen_char['name'].lower():
        print(f"🎉 Excellent! It was {chosen_char['name']}!")
    else:
        print(f"💡 Good try! I was thinking of {chosen_char['name']}!")
    
    press_enter_to_continue()

def demonstrate_input_validation(name):
    """Teach input validation with loops"""
    clear_screen()
    print("✅ INPUT VALIDATION - Making Programs Robust")
    print("=" * 45)
    
    print(f"\n{name}, let's learn how to handle user input properly!")
    print("💡 We need to make sure users give us valid data!")
    
    print("\n📝 Example: Getting a positive number of adventures")
    print("while True:")
    print("    adventures = int(input('How many adventures? '))")
    print("    if adventures > 0:")
    print("        break")
    print("    print('Please enter a positive number!')")
    
    print("\n🎮 Let's try it! Plan some Famous Five adventures:")
    
    while True:
        try:
            adventures = int(input("🗺️ How many adventures should the Famous Five go on? "))
            if adventures > 0:
                break
            print("🤔 The Famous Five need at least one adventure!")
        except ValueError:
            print("🔢 Please enter a valid number!")
    
    print(f"\n🎉 Perfect! The Famous Five will go on {adventures} adventures!")
    
    # Demonstrate the adventures
    adventure_types = ["Treasure hunt", "Mystery solving", "Island exploration", "Cave discovery", "Secret passage"]
    
    print(f"\n📚 Here are their {adventures} adventures:")
    for i in range(adventures):
        adventure = random.choice(adventure_types)
        print(f"   {i + 1}. {adventure} 🕵️")
        time.sleep(0.5)
    
    press_enter_to_continue()

def demonstrate_mario_blocks(name):
    """Teach nested loops with block patterns"""
    clear_screen()
    print("🧱 PATTERN MAKING - Peter's Garden Wall")
    print("=" * 35)
    
    print(f"\n{name}, let's help Peter build patterns in his garden!")
    print("💡 We'll use nested loops to create rows and columns!")
    
    # Single column
    print("\n📝 First, a simple column of carrots:")
    print("for _ in range(3):")
    print("    print('🥕')")
    
    print("\n🎬 Result:")
    for _ in range(3):
        print("🥕")
        time.sleep(0.3)
    
    # Single row
    print(f"\n📝 Now, a row of carrots:")
    print("print('🥕' * 4)")
    
    print("\n🎬 Result:")
    print("🥕" * 4)
    
    # Square pattern
    size = get_positive_integer(f"\n🎯 {name}, how big should Peter's garden patch be? (1-5): ", max_val=5)
    
    print(f"\n📝 Creating a {size}x{size} garden patch:")
    print("for row in range(size):")
    print("    for col in range(size):")
    print("        print('🥕', end='')")
    print("    print()  # New line after each row")
    
    print(f"\n🌱 Peter's {size}x{size} garden patch:")
    for row in range(size):
        for col in range(size):
            print("🥕", end="")
            time.sleep(0.1)
        print()
    
    press_enter_to_continue()

def get_positive_integer(prompt, max_val=None):
    """Get a positive integer from user with validation"""
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                if max_val and num > max_val:
                    print(f"🎯 Please enter a number between 1 and {max_val}!")
                    continue
                return num
            print("🔢 Please enter a positive number!")
        except ValueError:
            print("🔢 Please enter a valid number!")

def final_challenge(name):
    """A fun final challenge combining all concepts"""
    clear_screen()
    print("🏆 FINAL CHALLENGE - The Grand Adventure!")
    print("=" * 40)
    
    print(f"\n🎉 Congratulations {name}! Let's combine everything you've learned!")
    print("🎯 Challenge: Create a story with all our character groups!")
    
    # Get user preferences
    num_characters = get_positive_integer("👥 How many characters should join the adventure? (1-5): ", max_val=5)
    
    # Combine all characters
    all_characters = PETER_RABBIT_CHARACTERS + FAMOUS_FIVE_CHARACTERS + FARAWAY_TREE_CHARACTERS
    
    # Let user pick characters
    chosen_characters = []
    print(f"\n📋 Available characters: {', '.join(all_characters)}")
    
    for i in range(num_characters):
        while True:
            char = input(f"🌟 Choose character #{i + 1}: ").strip()
            if char in all_characters and char not in chosen_characters:
                chosen_characters.append(char)
                break
            elif char in chosen_characters:
                print(f"🤔 {char} is already chosen! Pick someone else.")
            else:
                print(f"🔍 I don't know {char}. Try: {', '.join(all_characters)}")
    
    # Create adventure story
    print(f"\n📖 THE GRAND ADVENTURE OF {', '.join(chosen_characters).upper()}!")
    print("=" * 50)
    
    adventure_locations = ["Enchanted Forest", "Secret Island", "Magic Garden", "Moonlit Meadow", "Crystal Cave"]
    location = random.choice(adventure_locations)
    
    print(f"\n🗺️ Our heroes meet at the {location}...")
    
    # Character introductions with dictionary
    char_actions = {
        "Peter": "hops excitedly and sniffs for carrots 🐰🥕",
        "Julian": "takes charge and studies the map 🗺️",
        "Silky": "sprinkles fairy dust and giggles ✨",
        "Moonface": "offers pop cakes to everyone 🍰",
        "George": "whistles for Timmy 🐕",
        "Jo": "looks for the nearest tree to climb 🌳"
    }
    
    print(f"\n🎭 Character introductions:")
    for i, character in enumerate(chosen_characters, 1):
        action = char_actions.get(character, "waves hello and smiles 👋")
        print(f"   {i}. {character} {action}")
        time.sleep(1)
    
    # Adventure sequence
    print(f"\n🎪 The Adventure Unfolds:")
    adventures = ["discovered a hidden treasure", "solved an ancient riddle", "befriended a magical creature", "found a secret passage"]
    
    for i, adventure in enumerate(adventures[:len(chosen_characters)], 1):
        responsible_char = chosen_characters[(i-1) % len(chosen_characters)]
        print(f"   Chapter {i}: {responsible_char} {adventure}! 🌟")
        time.sleep(1)
    
    print(f"\n🎊 And they all lived happily ever after!")
    print(f"💫 Thanks for joining the adventure, {name}!")

def main():
    """Main program function"""
    # Welcome and setup
    name = get_user_name()
    
    print(f"\n🎉 Welcome to Python Programming, {name}!")
    print("🐍 Today we'll learn with beloved storybook characters!")
    
    ready = input(f"\n🚀 Ready to start your Python journey, {name}? (yes/no): ").lower()
    if ready not in ['yes', 'y', 'yeah', 'yep']:
        print("💝 No worries! Come back when you're ready to learn Python! 👋")
        return
    
    # Learning modules
    modules = [
        ("🐰 Basic Loops with Peter Rabbit", demonstrate_basic_loops),
        ("🌟 For Loops - The Elegant Way", demonstrate_for_loops),
        ("📝 Lists with the Famous Five", demonstrate_lists),
        ("🔧 Advanced List Operations", demonstrate_list_operations),
        ("📚 Dictionaries - Character Profiles", demonstrate_dictionaries),
        ("🎭 Complex Data Structures", demonstrate_complex_dictionaries),
        ("✅ Input Validation Techniques", demonstrate_input_validation),
        ("🧱 Pattern Making with Nested Loops", demonstrate_mario_blocks),
        ("🏆 Final Challenge - Grand Adventure", final_challenge)
    ]
    
    for i, (title, func) in enumerate(modules, 1):
        print(f"\n📚 Module {i}: {title}")
        continue_learning = input("🎯 Continue? (yes/skip/quit): ").lower()
        
        if continue_learning in ['quit', 'q', 'exit']:
            print(f"👋 Thanks for learning Python with us, {name}! Keep coding! 🐍")
            break
        elif continue_learning in ['skip', 's']:
            print("⏭️ Skipping to next module...")
            continue
        
        func(name)
    
    # Final message
    clear_screen()
    print("🎓 CONGRATULATIONS! 🎓")
    print("=" * 25)
    print(f"\n🌟 Well done, {name}! You've completed the Python learning adventure!")
    print("\n📚 Topics you've mastered:")
    print("   ✅ While loops and for loops")
    print("   ✅ Lists and list operations")
    print("   ✅ Dictionaries and data structures")
    print("   ✅ Input validation patterns")
    print("   ✅ Nested loops and patterns")
    print("   ✅ String manipulation")
    print("   ✅ Programming best practices")
    
    print(f"\n🐍 Keep practicing Python, {name}! The adventure continues...")
    print("💫 Remember: Peter, the Famous Five, and the Faraway Tree friends")
    print("   are always here to help you learn! 🐰👥🌳")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for learning Python with us! See you next time! 🐍")
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        print("🔧 Don't worry, even experienced programmers encounter errors!")
        print("💡 This is all part of the learning process!")